from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "U1")
class RollerToPos1Command(SerialCommand):
    def run(self):
        print("RollerToPos1")
        self.ser.write(b"OK\r\n")
