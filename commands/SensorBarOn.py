from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "O1")
class SensorBarOnCommand(SerialCommand):
    def run(self):
        print("SensorBarOn")
        self.ser.write(b"OK\r\n")
