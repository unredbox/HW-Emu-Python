from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "T5")
class RollerToPos5Command(SerialCommand):
    def run(self):
        print("RollerToPos5")
        self.ser.write(b"OK\r\n")
