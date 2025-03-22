from typing import Union

from hal_hw_emu.arcus.common import serial_command
from hal_hw_emu.arcus.SerialCommand import SerialCommand


@serial_command("E(?P<axis>X|Y)(=(?P<value>\d+))*", "E", "Return or set encoder position of axis motor")
class ECommand(SerialCommand):
    def run(self, axis: str, value: Union[int, None] = None):
        self.logger.debug(f"E; Axis {axis}, Value {value}")
        if not value:
            # get
            # TODO:
            # dummy 24 bit signed number
            a = bytes([0x12, 0x34, 0x56])
            self.ser.write(a + b"\x04")
        else:
            # set
            self.ser.write(b"\x04")
