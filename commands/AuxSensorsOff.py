from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Aux, "P1")
class AuxSensorsOffCommand(SerialCommand):
    def run(self):
        print("AuxSensorsOff")
        self.ser.write(b"OK\r\n")
