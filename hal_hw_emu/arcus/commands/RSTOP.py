from typing import Union

from hal_hw_emu.arcus.common import serial_command
from hal_hw_emu.arcus.SerialCommand import SerialCommand


@serial_command("RSTOP(?P<axis>X|Y|Z|U)*", "RSTOP", "Stop all motors or a specific axis")
class RStopCommand(SerialCommand):
    def run(self, axis: Union[str, None] = None):
        self.logger.debug(f"RStop; Axis {axis}")
        self.ser.write(b"\x04")
