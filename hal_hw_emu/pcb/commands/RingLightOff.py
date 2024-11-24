from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "P2")
class RingLightOffCommand(SerialCommand):
    def run(self):
        self.logger.debug("RingLightOff")
        self.ser.write(b"O OK\r\n")
