from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Aux, "V")
class VendDoorRentCommand(SerialCommand):
    def run(self):
        print("VendDoorRent")
        self.ser.write(b"OK\r\n")
