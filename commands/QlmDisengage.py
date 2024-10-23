from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Aux, "L1")
class QlmDisengageCommand(SerialCommand):
    def run(self):
        print("QlmDisengage")
        self.ser.write(b"OK\r\n")
