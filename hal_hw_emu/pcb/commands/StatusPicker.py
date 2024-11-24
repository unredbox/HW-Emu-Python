from hal_hw_emu.pcb.common import BitString, BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "S")
class StatusPickerCommand(SerialCommand):
    def run(self):
        self.logger.debug("StatusPicker")
        bitstring = BitString(20, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.ser.write(f"{bitstring}S OK\r\n".encode("ascii"))
