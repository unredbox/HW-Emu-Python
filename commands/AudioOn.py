from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Serial, "I")
class AudioOnCommand(SerialCommand):
    def run(self):
        print("AudioOn")
        self.ser.write(b"OK\r\n")
