from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "M1")
class GripperRetractCommand(SerialCommand):
    def run(self):
        print("GripperRetract")
        self.ser.write(b"OK\r\n")
