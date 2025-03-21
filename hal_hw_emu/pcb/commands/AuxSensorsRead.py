from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Aux, "R")
class AuxSensorsReadCommand(SerialCommand):
    def run(self):
        self.logger.debug("AuxSensorsRead")
        # bitstring = BitString(20, [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0])
        bitstring = self.registry.state.AUX_INPUTS
        self.ser.write(f"{bitstring}R OK\r\n".encode("ascii"))
