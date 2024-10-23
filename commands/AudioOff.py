from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Serial, "J")
class AudioOffCommand(SerialCommand):
    def run(self):
        print("AudioOff")
        self.ser.write(b"OK\r\n")
