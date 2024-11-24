from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Aux, "V")
class VendDoorRentCommand(SerialCommand):
    def run(self):
        self.logger.debug("VendDoorRent")
        self.ser.write(b"V OK\r\n")
