import board
import digitalio
import time
import microcontroller
import busio
import usb_hid
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# --- Inicializa controle HID ---
cc = ConsumerControl(usb_hid.devices)

# --- Configuração dos botões físicos ---
# botao = digitalio.DigitalInOut(board.GP2)
# botao.direction = digitalio.Direction.INPUT
# botao.pull = digitalio.Pull.UP

sw_a = digitalio.DigitalInOut(board.GP18)
sw_b = digitalio.DigitalInOut(board.GP19)
for p in (sw_a, sw_b):
    p.direction = digitalio.Direction.INPUT
    p.pull = digitalio.Pull.UP

# --- Lê boot anterior ---
try:
    with open("/bootchoice.txt", "r") as f:
        prevBoot = f.read().strip()
    print("\nBoot Choice:", prevBoot)
except OSError:
    print("Arquivo bootchoice.txt não encontrado.")
    prevBoot = "undefined"

# --- Atualiza arquivo de boot ---
def update_bootchoice():
    if not sw_a.value and sw_b.value:
        return "Linux"
    elif sw_a.value and not sw_b.value:
        return "MacOS"
    elif not sw_a.value and not sw_b.value:
        return "Windows"
    else:
        return "undefined"

# --- Inicializa APDS9960 no lado esquerdo ---
i2c = busio.I2C(board.GP27, board.GP26)  # SCL, SDA
apds = APDS9960(i2c)

apds.enable_proximity = True
apds.enable_gesture = True

# Sensibilidade
apds.gesture_prox_enter_thresh = 40
apds.gesture_prox_exit_thresh = 30
apds.gesture_gain = 2
apds.gesture_led_drive = 2

print("Sensor de gestos pronto! (lado esquerdo)")

# --- Função para gestos de volume ---
def handle_volume_gesture(gesture):
    if gesture == 0x01:   # UP
        print("🔊 Volume +")
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
    elif gesture == 0x02: # DOWN
        print("🔉 Volume -")
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
    elif gesture in (0x03, 0x04): # LEFT ou RIGHT
        print("🔇 Mute/Unmute")
        cc.send(ConsumerControlCode.MUTE)

# --- Loop principal ---
while True:
    # --- Controle de boot físico ---
    bootchoice = update_bootchoice()
    if prevBoot != bootchoice:
        print(f"Alteração detectada ({bootchoice}), reiniciando...")
        time.sleep(0.2)
        microcontroller.reset()

    # --- Controle de volume por gesto ---
    gesture = apds.gesture()
    if gesture is not None:
        handle_volume_gesture(gesture)
        time.sleep(0.4)

    time.sleep(0.05)
