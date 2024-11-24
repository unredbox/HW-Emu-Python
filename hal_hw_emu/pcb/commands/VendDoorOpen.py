from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Aux, "M2")
class VendDoorOpenCommand(SerialCommand):
    def run(self):
        self.logger.debug("VendDoorOpen")
        self.ser.write(b"M OK\r\n")
