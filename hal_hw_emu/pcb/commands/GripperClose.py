from hal_hw_emu.pcb.common import BoardAddress, InputState, PickerStatus, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "L3")
class GripperCloseCommand(SerialCommand):
    def run(self):
        self.logger.debug("GripperClose")
        self.registry.state_manager.picker_status.set_bit(PickerStatus.GripperClose, InputState.Active)
        self.registry.state_manager.picker_status.set_bit(PickerStatus.GripperOpen, InputState.Inactive)
        self.registry.state_manager.picker_status.set_bit(PickerStatus.GripperRent, InputState.Inactive)
        self.ser.write(b"L OK\r\n")
