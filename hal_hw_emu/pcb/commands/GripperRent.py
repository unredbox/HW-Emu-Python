from hal_hw_emu.pcb.common import BoardAddress, InputState, PickerStatus, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "V")
class GripperRentCommand(SerialCommand):
    def run(self):
        self.logger.debug("GripperRent")
        self.registry.state_manager.picker_status.set_bit(PickerStatus.GripperRent, InputState.Active)
        self.registry.state_manager.picker_status.set_bit(PickerStatus.GripperClose, InputState.Inactive)
        self.registry.state_manager.picker_status.set_bit(PickerStatus.GripperOpen, InputState.Inactive)
        self.ser.write(b"V OK\r\n")
