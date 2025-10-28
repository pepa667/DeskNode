import board
import storage
import os
import digitalio

# Ensure the CIRCUITPY drive is writable by your code
# This is necessary if you've made the drive read-only over USB
# for some reason, but by default it is usually writable by code.
# You might not need this if you haven't explicitly set read-only mode.
# If you do need it, uncomment the following line:
# storage.remount("/", readonly=False)
storage.remount("/", readonly=True)
storage.disable_usb_drive()

sw_a = digitalio.DigitalInOut(board.GP3)
sw_b = digitalio.DigitalInOut(board.GP4)
for p in (sw_a, sw_b):
    p.direction = digitalio.Direction.INPUT
    p.pull = digitalio.Pull.UP

# --- Atualiza arquivo de boot ---

def update_bootchoice():
    try:
        if not sw_a.value and sw_b.value:
            mode = "Linux"
        elif sw_a.value and not sw_b.value:
            mode = "MacOS"
        elif not sw_a.value and not sw_b.value:
            mode = "Windows"
        else:
            mode = "undefined"
        with open("/bootchoice.txt", "w") as f:
            f.write(mode)
	with open("/bootchoice.conf", "w") as f:
            f.write(f"default_selection {mode}\n")
        return mode
    except OSError as e:
        print(f"Error writing file: {e}")
        return "error"

boot_mode = update_bootchoice()
print(f"Boot inicial: {boot_mode}")


storage.remount("/", readonly=False)
storage.enable_usb_drive()
print(">> Modo de edição habilitado via USB.")
