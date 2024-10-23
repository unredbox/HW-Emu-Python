from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "O3")
class FraudSensorDisableTransistorCommand(SerialCommand):
    def run(self):
        print("FraudSensorDisableTransistor")
        self.ser.write(b"OK\r\n")
