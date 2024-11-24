from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "M1")
class GripperRetractCommand(SerialCommand):
    def run(self):
        self.logger.debug("GripperRetract")
        self.ser.write(b"M OK\r\n")
