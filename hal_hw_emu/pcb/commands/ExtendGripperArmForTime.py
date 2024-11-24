from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "I1")
class ExtendGripperArmForTimeCommand(SerialCommand):
    def run(self):
        self.logger.debug("ExtendGripperArmForTime")
        self.ser.write(b"I OK\r\n")
