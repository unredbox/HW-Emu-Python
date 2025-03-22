from hal_hw_emu.arcus.common import serial_command
from hal_hw_emu.arcus.SerialCommand import SerialCommand


@serial_command("ACCEL\s(?P<speed>\d+)", "ACCEL", "Set acceleration time in ms")
class LSPDCommand(SerialCommand):
    def run(self, speed: str):
        self.logger.debug(f"ACCEL; Value {speed}")
        self.ser.write(b"\x04")
