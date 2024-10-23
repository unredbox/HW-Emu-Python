from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Aux, "J2")
class UnknownVendDoorCloseCommand(SerialCommand):
    def run(self):
        print("UnknownVendDoorClose")
        self.ser.write(b"OK\r\n")
