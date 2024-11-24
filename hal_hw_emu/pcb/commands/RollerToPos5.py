from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


# Not used?
@serial_command(BoardAddress.Picker, "T5")
class RollerToPos5Command(SerialCommand):
    def run(self):
        self.logger.debug("RollerToPos5")
        self.ser.write(b"T OK\r\n")
