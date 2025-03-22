from hal_hw_emu.pcb.common import BoardAddress, InputState, PickerStatus, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "M1")
class GripperRetractCommand(SerialCommand):
    def run(self):
        self.logger.debug("GripperRetract")
        self.registry.state_manager.picker_status.set_bit(PickerStatus.GripperRetract, InputState.Active)
        self.registry.state_manager.picker_status.set_bit(PickerStatus.GripperExtend, InputState.Inactive)
        self.ser.write(b"M OK\r\n")
