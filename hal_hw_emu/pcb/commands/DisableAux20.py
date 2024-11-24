from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


# Not used?
@serial_command(BoardAddress.Aux, "P3")
class DisableAux20Command(SerialCommand):
    def run(self):
        self.logger.debug("DisableAux20")
        self.ser.write(b"OK\r\n")
