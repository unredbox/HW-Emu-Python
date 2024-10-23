from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "T6")
class RollerToPos6Command(SerialCommand):
    def run(self):
        print("RollerToPos6")
        self.ser.write(b"OK\r\n")
