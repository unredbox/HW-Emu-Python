from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Aux, "K2")
class VendDoorKillCommand(SerialCommand):
    def run(self):
        self.logger.debug("VendDoorKill")
        self.ser.write(b"K OK\r\n")
