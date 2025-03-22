from hal_hw_emu.arcus.common import serial_command
from hal_hw_emu.arcus.SerialCommand import SerialCommand


@serial_command("I(?P<offset>\d+)=(?P<value>\d+)", "I", "Set variable")
class ICommand(SerialCommand):
    def run(self, offset, value):
        self.logger.debug(f"I; Offset {offset}, Value {value}")
        self.ser.write(b"\x04")
