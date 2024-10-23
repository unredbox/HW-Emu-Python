from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "O1")
class Junction4OnCommand(SerialCommand):
    def run(self):
        print("Junction4On")
        self.ser.write(b"OK\r\n")
