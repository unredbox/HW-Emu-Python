from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "W")
class VersionPickerCommand(SerialCommand):
    def run(self):
        print("VersionPicker")
        self.ser.write(b"0.0.1\rOK\r\n")
