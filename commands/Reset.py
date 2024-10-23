from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Serial, "X")
class ResetCommand(SerialCommand):
    def run(self):
        print("Reset")
        self.ser.write(b"OK\r\n")
