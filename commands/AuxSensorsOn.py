from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Aux, "O1")
class AuxSensorsOnCommand(SerialCommand):
    def run(self):
        print("AuxSensorsOn")
        self.ser.write(b"OK\r\n")
