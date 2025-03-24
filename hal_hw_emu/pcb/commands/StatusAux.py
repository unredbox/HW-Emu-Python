from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Aux, "S")
class StatusAuxCommand(SerialCommand):
    def run(self):
        self.logger.debug("StatusAux")
        self.ser.write(f"{self.registry.state_manager.aux_status}S OK\r\n".encode("ascii"))
