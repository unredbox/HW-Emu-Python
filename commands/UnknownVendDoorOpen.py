from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Aux, "I2")
class UnknownVendDoorOpenCommand(SerialCommand):
    def run(self):
        print("UnknownVendDoorOpen")
        self.ser.write(b"OK\r\n")
