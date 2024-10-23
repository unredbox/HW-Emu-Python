from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "L3")
class GripperCloseCommand(SerialCommand):
    def run(self):
        print("GripperClose")
        self.ser.write(b"OK\r\n")
