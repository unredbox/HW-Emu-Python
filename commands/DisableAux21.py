from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Aux, "P4")
class DisableAux21Command(SerialCommand):
    def run(self):
        print("DisableAux21")
        self.ser.write(b"OK\r\n")
