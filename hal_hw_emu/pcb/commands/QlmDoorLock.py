from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


# Not used
@serial_command(BoardAddress.Aux, "P2")
class QlmDoorLockCommand(SerialCommand):
    def run(self):
        self.logger.debug("QlmHalt")
        self.ser.write(b"P OK\r\n")
