from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Aux, "O1")
class AuxSensorsOnCommand(SerialCommand):
    def run(self):
        self.logger.debug("AuxSensorsOn")
        self.ser.write(b"OK\r\n")
