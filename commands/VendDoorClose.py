from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Aux, "L2")
class VendDoorCloseCommand(SerialCommand):
    def run(self):
        print("VendDoorClose")
        self.ser.write(b"OK\r\n")
