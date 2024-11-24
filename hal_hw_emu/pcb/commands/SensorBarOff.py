from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "P1")
class SensorBarOffCommand(SerialCommand):
    def run(self):
        self.logger.debug("SensorBarOff")
        self.ser.write(b"O OK\r\n")
