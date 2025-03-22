from hal_hw_emu.arcus.common import serial_command
from hal_hw_emu.arcus.SerialCommand import SerialCommand


@serial_command("HOME(?P<axis>X|Y)(?P<direction>-|\+)", "HOME")
class HomeCommand(SerialCommand):
    def run(self, axis: str, direction: str):
        self.logger.debug(f"Home; Axis {axis}, Direction {direction}")
        self.ser.write(b"\x04")
