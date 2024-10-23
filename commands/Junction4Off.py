from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "P1")
class Junction4OffCommand(SerialCommand):
    def run(self):
        print("Junction4Off")
        self.ser.write(b"OK\r\n")
