from hal_hw_emu.pcb.common import BitString, BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "R")
class ReadPickerInputsCommand(SerialCommand):
    def run(self):
        self.logger.debug("ReadPickerInputs")
        bitstring = BitString(20, [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0])
        self.ser.write(f"{bitstring}R OK\r\n".encode("ascii"))
