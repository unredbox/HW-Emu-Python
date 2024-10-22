# HAL-Emulator-Python

A tool for emulating the hardware that the Hardware Abstraction Layer (HAL) talks to.

-   pcb.py - This emulates the PCB, AUX, SER and QR boards, which runs on COM1
-   arcus.py - This emulates the Arcus stepper motion controller

# Usage

-   install python from [this fork](https://github.com/NulAsh/cpython/releases/tag/v3.10.1win7-1)
-   install the requirements: `pip install -r requirements.txt`
-   setup a virtual com port with something like [VirtualSerialPort](https://www.virtual-serial-port.org/) in split mode
    -   if using VSP, use a split type with COM1 -> COM10, and COM3 -> COM13
-   start the scripts in 2 different command prompts:
    -   `python pcb.py`
    -   `python arcus.py`
-   start or restart the HAL service
