from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "M2")
class TrackOpenCommand(SerialCommand):
    def run(self):
        print("TrackOpen")
        self.ser.write(b"OK\r\n")
