from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Aux, "P3")
class DisableAux20Command(SerialCommand):
    def run(self):
        print("DisableAux20")
        self.ser.write(b"OK\r\n")
