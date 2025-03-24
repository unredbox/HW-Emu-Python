from hal_hw_emu.pcb.common import BitString, BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "R")
class ReadPickerInputsCommand(SerialCommand):
    def run(self):
        self.logger.debug("ReadPickerInputs")
        self.ser.write(f"{self.registry.state_manager.picker_inputs}R OK\r\n".encode("ascii"))
