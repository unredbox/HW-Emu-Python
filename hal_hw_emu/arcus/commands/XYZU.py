from hal_hw_emu.arcus.common import serial_command
from hal_hw_emu.arcus.SerialCommand import SerialCommand


@serial_command("(?P<axis>X|Y|Z|U)(?P<value>[-\d]+)", "XYZU", "Move axis to location")
class XYZUCommand(SerialCommand):
    def run(self, axis: str, value: int):
        self.logger.debug(f"XYZU; Axis {axis}, Value {value}")
        self.ser.write(b"\x04")
