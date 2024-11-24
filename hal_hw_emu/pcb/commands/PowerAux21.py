from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


# Not used?
@serial_command(BoardAddress.Aux, "O4")
class PowerAux21Command(SerialCommand):
    def run(self):
        self.logger.debug("PowerAux21")
        self.ser.write(b"O OK\r\n")
