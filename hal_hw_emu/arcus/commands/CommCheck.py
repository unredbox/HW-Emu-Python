from hal_hw_emu.arcus.common import serial_command
from hal_hw_emu.arcus.SerialCommand import SerialCommand


@serial_command("$")
class CommCheckCommand(SerialCommand):
    def run(self):
        self.logger.debug("CommCheck")
        self.ser.write(b"OK\x04")
