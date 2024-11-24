from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "O2")
class RingLightOnCommand(SerialCommand):
    def run(self):
        self.logger.debug("RingLightOn")
        self.ser.write(b"O OK\r\n")
