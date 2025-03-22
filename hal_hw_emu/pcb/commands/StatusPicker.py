from hal_hw_emu.pcb.common import BoardAddress, PickerStatus, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "S")
class StatusPickerCommand(SerialCommand):
    def run(self):
        self.logger.debug("StatusPicker")
        print(self.registry.state_manager.picker_status.is_bit_set(PickerStatus.TrackOpen))
        self.ser.write(f"{self.registry.state_manager.picker_status}S OK\r\n".encode("ascii"))
