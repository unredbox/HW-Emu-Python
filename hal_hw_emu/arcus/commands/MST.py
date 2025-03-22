from hal_hw_emu.arcus import SerialCommand
from hal_hw_emu.arcus.common import serial_command


@serial_command(r"MST(?P<axis>X|Y)", "MST", "Get motor status")
class MotorStatusCommand(SerialCommand):
    def run(self, axis: str):
        self.logger.debug(f"MotorStatus; Axis {axis}")
        self.ser.write(b"\x2f\x04")
