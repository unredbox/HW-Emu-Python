from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Aux, "L2")
class VendDoorCloseCommand(SerialCommand):
    def run(self):
        self.logger.debug("VendDoorClose")
        self.ser.write(b"L OK\r\n")
