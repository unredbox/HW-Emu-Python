from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Serial, "I")
class AudioOnCommand(SerialCommand):
    def run(self):
        self.logger.debug("AudioOn")
        self.ser.write(b"OK\r\n")
