from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


# Not used?
@serial_command(BoardAddress.Aux, "J2")
class UnknownVendDoorCloseCommand(SerialCommand):
    def run(self):
        self.logger.debug("UnknownVendDoorClose")
        self.ser.write(b"J OK\r\n")
