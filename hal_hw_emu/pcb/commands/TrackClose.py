from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "L2")
class TrackCloseCommand(SerialCommand):
    def run(self):
        self.logger.debug("TrackClose")
        self.ser.write(b"L OK\r\n")
