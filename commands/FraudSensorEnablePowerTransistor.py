from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "O4")
class FraudSensorEnablePowerTransistorCommand(SerialCommand):
    def run(self):
        print("FraudSensorEnablePowerTransistor")
        self.ser.write(b"OK\r\n")
