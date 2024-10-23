from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "P2")
class RingLightOffCommand(SerialCommand):
    def run(self):
        print("RingLightOff")
        self.ser.write(b"OK\r\n")
