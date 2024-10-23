from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "I4")
class RollerOutCommand(SerialCommand):
    def run(self):
        print("RollerOut")
        self.ser.write(b"OK\r\n")
