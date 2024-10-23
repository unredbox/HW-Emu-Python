from commands.SerialCommand import SerialCommand
from common import BitString, BoardAddress, serial_command


@serial_command(BoardAddress.Aux, "R")
class AuxSensorsReadCommand(SerialCommand):
    def run(self):
        print("AuxSensorsRead")
        bitstring = BitString(20, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.ser.write(f"{bitstring}\rOK\r\n".encode("ascii"))
