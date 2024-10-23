from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Aux, ":1")
class QlmDropCommand(SerialCommand):
    def run(self):
        print("QlmDrop")
        self.ser.write(b"OK\r\n")
