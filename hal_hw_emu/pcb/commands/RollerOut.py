from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "I4")
class RollerOutCommand(SerialCommand):
    def run(self):
        self.logger.debug("RollerOut")
        self.ser.write(b"I OK\r\n")
