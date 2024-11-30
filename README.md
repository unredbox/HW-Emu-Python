# HAL-Emulator-Python

A tool for emulating the hardware that the Hardware Abstraction Layer (HAL) talks to.

-   pcb.py - This emulates the PCB, AUX, SER and QR boards, which runs on COM1
-   arcus.py - This emulates the Arcus stepper motion controller

# Usage

-   install python from [this fork](https://github.com/NulAsh/cpython/releases/tag/v3.10.1win7-1)
-   install the requirements: `pip install -r requirements.txt`
-   Setup a virtual com port with something like [com0com](https://sourceforge.net/projects/com0com/)
    -   Setup pairs if COM1 -> COM10, and COM3 -> COM13
-   start the scripts in 2 different command prompts:
    -   `python pcb.py`
    -   `python arcus.py`
-   start or restart the HAL service
