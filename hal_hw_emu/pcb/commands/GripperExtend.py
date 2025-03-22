from hal_hw_emu.pcb.common import BoardAddress, InputState, PickerStatus, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "L1")
class GripperExtendCommand(SerialCommand):
    def run(self):
        self.logger.debug("GripperExtend")
        self.registry.state_manager.picker_status.set_bit(PickerStatus.GripperExtend, InputState.Active)
        self.registry.state_manager.picker_status.set_bit(PickerStatus.GripperRetract, InputState.Inactive)
        self.ser.write(b"L OK\r\n")
