from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Aux, "R")
class AuxSensorsReadCommand(SerialCommand):
    def run(self):
        self.logger.debug("AuxSensorsRead")
        self.ser.write(f"{self.registry.state_manager.aux_inputs}R OK\r\n".encode("ascii"))
