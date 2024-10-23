from commands.SerialCommand import SerialCommand
from common import BoardAddress, serial_command


@serial_command(BoardAddress.Picker, "P4")
class FraudSensorDisablePowerTransistorCommand(SerialCommand):
    def run(self):
        print("FraudSensorDisablePowerTransistor")
        self.ser.write(b"OK\r\n")
