from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


# Not used?
@serial_command(BoardAddress.Picker, "U3")
class RollerToPos3Command(SerialCommand):
    def run(self):
        self.logger.debug("RollerToPos3")
        self.ser.write(b"U OK\r\n")
