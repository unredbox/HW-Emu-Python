from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "K4")
class RollerStopCommand(SerialCommand):
    def run(self):
        print("RollerStop")
        self.ser.write(b"OK\r\n")
