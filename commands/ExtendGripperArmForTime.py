from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "I1")
class ExtendGripperArmForTimeCommand(SerialCommand):
    def run(self):
        print("ExtendGripperArmForTime")
        self.ser.write(b"OK\r\n")
