from hal_hw_emu.pcb.common import BoardAddress, InputState, PickerStatus, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "M3")
class GripperOpenCommand(SerialCommand):
    def run(self):
        self.logger.debug("GripperOpen")
        self.registry.state_manager.picker_status.set_bit(PickerStatus.GripperOpen, InputState.Active)
        self.registry.state_manager.picker_status.set_bit(PickerStatus.GripperClose, InputState.Inactive)
        self.registry.state_manager.picker_status.set_bit(PickerStatus.GripperRent, InputState.Inactive)
        self.ser.write(b"M OK\r\n")
