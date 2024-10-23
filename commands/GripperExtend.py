from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "L1")
class GripperExtendCommand(SerialCommand):
    def run(self):
        print("GripperExtend")
        self.ser.write(b"OK\r\n")
