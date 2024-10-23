from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "L2")
class TrackCloseCommand(SerialCommand):
    def run(self):
        print("TrackClose")
        self.ser.write(b"OK\r\n")
