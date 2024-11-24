from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "K4")
class RollerStopCommand(SerialCommand):
    def run(self):
        self.logger.debug("RollerStop")
        self.ser.write(b"K OK\r\n")
