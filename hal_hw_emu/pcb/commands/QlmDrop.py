from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


# Not used
@serial_command(BoardAddress.Aux, "L1")
class QlmDropCommand(SerialCommand):
    def run(self):
        self.logger.debug("QlmDrop")
        self.ser.write(b"L OK\r\n")
