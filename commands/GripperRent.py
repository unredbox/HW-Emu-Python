from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "V")
class GripperRentCommand(SerialCommand):
    def run(self):
        print("GripperRent")
        self.ser.write(b"OK\r\n")
