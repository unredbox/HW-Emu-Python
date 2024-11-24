from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "K1")
class GripperExtendHaltCommand(SerialCommand):
    def run(self):
        self.logger.debug("GripperExtendHalt")
        self.ser.write(b"K OK\r\n")
