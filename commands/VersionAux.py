from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Aux, "W")
class VersionAuxCommand(SerialCommand):
    def run(self):
        print("VersionAux")
        self.ser.write(b"0.0.1\rOK\r\n")
