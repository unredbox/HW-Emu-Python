from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "M3")
class GripperOpenCommand(SerialCommand):
    def run(self):
        print("GripperOpen")
        self.ser.write(b"OK\r\n")
