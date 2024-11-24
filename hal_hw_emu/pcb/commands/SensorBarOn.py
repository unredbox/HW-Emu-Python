from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "O1")
class SensorBarOnCommand(SerialCommand):
    def run(self):
        self.logger.debug("SensorBarOn")
        self.ser.write(b"O OK\r\n")
