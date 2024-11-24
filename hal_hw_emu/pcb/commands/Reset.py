from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Serial, "X")
class ResetCommand(SerialCommand):
    def run(self):
        self.logger.debug("Reset")
        self.ser.write(b"OK\r\n")
