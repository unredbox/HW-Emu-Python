from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "P1")
class SensorBarOffCommand(SerialCommand):
    def run(self):
        print("SensorBarOff")
        self.ser.write(b"OK\r\n")
