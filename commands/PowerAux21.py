from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Aux, "O4")
class PowerAux21Command(SerialCommand):
    def run(self):
        print("PowerAux21")
        self.ser.write(b"OK\r\n")
