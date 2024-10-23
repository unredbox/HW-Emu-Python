from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "U3")
class RollerToPos3Command(SerialCommand):
    def run(self):
        print("RollerToPos3")
        self.ser.write(b"OK\r\n")
