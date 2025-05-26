# HAL-Emulator-Python

A tool for emulating the hardware that the Hardware Abstraction Layer (HAL) talks to.

-   pcb.py - This emulates the PCB, AUX, SER and QR boards, which runs on COM1
-   arcus.py - This emulates the Arcus stepper motion controller, which runs on COM3

# Usage
The easiest way is to run this in the Virtual Machine (if you are using one), however you could also use serial port forwarding to run it on the host instead

-   Install Python
      - If you are using Windows 7, use [this fork](https://github.com/NulAsh/cpython/releases/tag/v3.10.1win7-1)
      - Otherwise you can use the latest version from [python.org](https://www.python.org/downloads/)
-   Install the requirements: `pip install -r requirements.txt`
-   Setup the required virtual COM ports with something like [com0com](https://sourceforge.net/projects/com0com/)
    -   Setup pairs of COM1 -> COM10, and COM3 -> COM13
-   Start the scripts in 2 different command prompts:
    -   `python pcb.py`
    -   `python arcus.py`
-   Start or restart the HAL service using services.msc or cmd

You may also be interested in looking at [V2](https://github.com/unredbox/HW-Emu-Python/tree/v2) which is better designed.
