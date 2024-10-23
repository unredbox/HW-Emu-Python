from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Aux, "O3")
class PowerAux20Command(SerialCommand):
    def run(self):
        print("PowerAux20")
        self.ser.write(b"OK\r\n")
