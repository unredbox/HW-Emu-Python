from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Aux, "K2")
class VendDoorKillCommand(SerialCommand):
    def run(self):
        print("VendDoorKill")
        self.ser.write(b"OK\r\n")
