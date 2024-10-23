from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "O2")
class RingLightOnCommand(SerialCommand):
    def run(self):
        print("RingLightOn")
        self.ser.write(b"OK\r\n")
