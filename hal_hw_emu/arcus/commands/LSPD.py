from hal_hw_emu.arcus.common import serial_command
from hal_hw_emu.arcus.SerialCommand import SerialCommand


@serial_command("LSPD\s(?P<speed>\d+)", "LSPD", "Set low pulse speed in pulses per second")
class LSPDCommand(SerialCommand):
    def run(self, speed: str):
        self.logger.debug(f"LSPD; Value {speed}")
        self.ser.write(b"\x04")
