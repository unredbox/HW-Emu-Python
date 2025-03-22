from hal_hw_emu.arcus.common import serial_command
from hal_hw_emu.arcus.SerialCommand import SerialCommand


@serial_command("INC", None, "Set the move mode to incremental")
class INCCommand(SerialCommand):
    def run(self):
        self.ser.write(b"\x04")
