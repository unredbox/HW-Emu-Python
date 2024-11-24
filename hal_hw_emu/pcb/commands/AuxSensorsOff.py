from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Aux, "P1")
class AuxSensorsOffCommand(SerialCommand):
    def run(self):
        self.logger.debug("AuxSensorsOff")
        self.ser.write(b"OK\r\n")
