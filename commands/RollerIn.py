from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "J4")
class RollerInCommand(SerialCommand):
    def run(self):
        print("RollerIn")
        self.ser.write(b"OK\r\n")
