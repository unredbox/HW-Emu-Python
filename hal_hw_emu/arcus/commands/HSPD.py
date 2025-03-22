from hal_hw_emu.arcus.common import serial_command
from hal_hw_emu.arcus.SerialCommand import SerialCommand


@serial_command("HSPD\s(?P<speed>\d+)", "HSPD", "Set high speed pulses per second")
class HSPDCommand(SerialCommand):
    def run(self, speed: str):
        self.logger.debug(f"HSPD; Value {speed}")
        self.ser.write(b"\x04")
