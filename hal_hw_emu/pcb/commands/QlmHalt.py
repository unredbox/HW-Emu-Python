from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


# Not used
@serial_command(BoardAddress.Aux, "K1")
class QlmHaltCommand(SerialCommand):
    def run(self):
        self.logger.debug("QlmHalt")
        self.ser.write(b"K OK\r\n")
