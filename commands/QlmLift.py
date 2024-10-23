from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Aux, "M1")
class QlmLiftCommand(SerialCommand):
    def run(self):
        print("QlmLift")
        self.ser.write(b"OK\r\n")
