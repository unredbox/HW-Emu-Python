from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Aux, "M2")
class VendDoorOpenCommand(SerialCommand):
    def run(self):
        print("VendDoorOpen")
        self.ser.write(b"OK\r\n")
