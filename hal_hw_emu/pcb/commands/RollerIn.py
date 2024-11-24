from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "J4")
class RollerInCommand(SerialCommand):
    def run(self):
        self.logger.debug("RollerIn")
        self.ser.write(b"J OK\r\n")
