from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Aux, "M1")
class QlmEngageCommand(SerialCommand):
    def run(self):
        print("QlmEngage")
        self.ser.write(b"OK\r\n")
