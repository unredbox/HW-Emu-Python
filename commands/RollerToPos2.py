from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "U2")
class RollerToPos2Command(SerialCommand):
    def run(self):
        print("RollerToPos2")
        self.ser.write(b"OK\r\n")
