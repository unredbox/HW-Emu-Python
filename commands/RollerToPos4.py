from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "T4")
class RollerToPos4Command(SerialCommand):
    def run(self):
        print("RollerToPos4")
        self.ser.write(b"OK\r\n")
