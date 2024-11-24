from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


# Not used?
@serial_command(BoardAddress.Aux, "P4")
class DisableAux21Command(SerialCommand):
    def run(self):
        self.logger.debug("DisableAux21")
        self.ser.write(b"OK\r\n")
