from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Serial, "Y")
class VersionSerialCommand(SerialCommand):
    def run(self):
        print("VersionSerial")
        self.ser.write(b"0.0.1\rOK\r\n")
