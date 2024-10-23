from commands.SerialCommand import SerialCommand
from common import BitString, BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "S")
class StatusPickerCommand(SerialCommand):
    def run(self):
        print("StatusPicker")
        bitstring = BitString(20, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.ser.write(f"{bitstring}\rOK\r\n".encode("ascii"))
