from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Aux, "K1")
class QlmHaltCommand(SerialCommand):
    def run(self):
        print("QlmHalt")
        self.ser.write(b"OK\r\n")
