from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "K1")
class GripperExtendHaltCommand(SerialCommand):
    def run(self):
        print("GripperExtendHalt")
        self.ser.write(b"OK\r\n")
