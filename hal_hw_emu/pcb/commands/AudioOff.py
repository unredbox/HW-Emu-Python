from hal_hw_emu.pcb import SerialCommand
from hal_hw_emu.pcb.common import BoardAddress, serial_command


@serial_command(BoardAddress.Serial, "J")
class AudioOffCommand(SerialCommand):
    def run(self):
        self.logger.debug("AudioOff")
        self.ser.write(b"OK\r\n")
