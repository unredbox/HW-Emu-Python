from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


# Not used?
@serial_command(BoardAddress.Picker, "T6")
class RollerToPos6Command(SerialCommand):
    def run(self):
        self.logger.debug("RollerToPos6")
        self.ser.write(b"T OK\r\n")
