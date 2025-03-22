from hal_hw_emu.arcus.common import serial_command
from hal_hw_emu.arcus.SerialCommand import SerialCommand


@serial_command("MIO(?P<axis>X|Y|Z|U)", "MIO", "Motor IO Status Value")
class ECommand(SerialCommand):
    def run(self, axis: str):
        self.logger.debug(f"MIO; Axis {axis}")
        # TODO:
        self.ser.write(b"\x17\x04")
