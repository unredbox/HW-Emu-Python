from hal_hw_emu.pcb.common import BitString, BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Aux, "S")
class StatusAuxCommand(SerialCommand):
    def run(self):
        self.logger.debug("StatusAux")
        bitstring = BitString(20, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.ser.write(f"{bitstring}S OK\r\n".encode("ascii"))
