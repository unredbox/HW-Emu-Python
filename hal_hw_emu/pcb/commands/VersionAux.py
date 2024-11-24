from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Aux, "W")
class VersionAuxCommand(SerialCommand):
    def run(self):
        self.logger.debug("VersionAux")
        self.ser.write(b" DAN LEIWE QLM'AUX CONTROLER GET_A_MOVIE 12/20/05 ADD 002 OK\r\n")
