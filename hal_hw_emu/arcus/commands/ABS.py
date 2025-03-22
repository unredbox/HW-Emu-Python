from hal_hw_emu.arcus.common import serial_command
from hal_hw_emu.arcus.SerialCommand import SerialCommand


@serial_command("ABS", None, "Set the move mode to absolute")
class ABSCommand(SerialCommand):
    def run(self):
        self.ser.write(b"\x04")
