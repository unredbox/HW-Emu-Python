from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


# Not used?
@serial_command(BoardAddress.Picker, "T4")
class RollerToPos4Command(SerialCommand):
    def run(self):
        self.logger.debug("RollerToPos4")
        self.ser.write(b"T OK\r\n")
