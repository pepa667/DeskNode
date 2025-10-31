# DeskNode

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Issues](https://img.shields.io/github/issues/Opus667/DeskNode)](https://github.com/Opus667/DeskNode/issues)

[![DeskNode](/Logo/DeskNode---Logo---Fundo-Escuro.gif)]

DeskNode is an open-source, modular control panel for PCs, designed for makers and hobbyists. It provides physical control over boot selection, volume/mute, power/reset, and expands USB connectivity.

---

## Table of Contents

- [Features](#features)
- [Hardware](#hardware)
- [Software](#software)
- [Usage](#usage)
- [License](#license)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

---

## Features

- **3-way toggle switch** for boot selection (e.g., Linux, macOS, Windows)
- **Boot configured via Raspberry Pi Pico**, writing `bootchoice.txt` to a USB drive read by **rEFInd**
- **Volume and mute control** via APDS-9960 gesture sensor
- **Power and reset buttons** for PC
- **Four-port USB extension hub**
- Fully open-source and modular

---

## Hardware

DeskNode integrates:

- **Controller:** Raspberry Pi Pico
- **Controls:**
  - 3-way toggle switch for boot selection
  - Gesture-based volume and mute control using APDS-9960
  - Power and reset buttons
- **USB Hub:** 4-port USB extension
- **Connections:** Direct integration with PC motherboard for power/reset/boot signaling, plus USB for rEFInd boot selection
- **Optional:** USB drive for configuration updates

> Wiring diagrams and schematics are provided in the [`/hardware`](hardware) folder.

---

## Software

- **Firmware:** CircuitPython sketches for Raspberry Pi Pico
- **Boot selection logic:** Pi Pico writes the chosen boot option to `bootchoice.txt` on a mounted USB drive. rEFInd reads this file to select the boot OS automatically.
- **Volume/mute control:** Reads gestures from APDS-9960 sensor and sends appropriate commands
- **Open-source license:** MIT recommended

> Firmware files can be found in the [`/firmware`](firmware) folder.

---

## Usage

- **Boot selection:** Set the 3-way toggle switch before powering on. The Pi Pico writes the selection to USB, which rEFInd uses to boot the chosen OS.
- **Volume/mute:** Control audio output via gestures detected by APDS-9960
- **Power/reset:** Use dedicated buttons
- **USB hub:** Plug devices into DeskNode USB ports
- **Configuration updates:** Insert USB drive with firmware/config files

---

## License

DeskNode is licensed under the **MIT License**, making it fully open source.  
See [LICENSE](LICENSE) for details.

---

## Contributing

Contributions are welcome! Please:

- Fork the repository
- Create feature branches
- Submit pull requests with clear descriptions

---

## Acknowledgements

- Maker and DIY hardware communities
- Adafruit APDS-9960 tutorials and examples
- rEFInd boot manager documentation
- Open-source microcontroller projects for inspiration
