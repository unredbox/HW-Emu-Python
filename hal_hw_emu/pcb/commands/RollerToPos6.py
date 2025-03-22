from hal_hw_emu.pcb.common import BoardAddress, InputState, PickerInput, PickerStatus, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


# Not used?
@serial_command(BoardAddress.Picker, "T6")
class RollerToPos6Command(SerialCommand):
    def run(self):
        self.logger.debug("RollerToPos6")
        # TODO: this is probably wrong
        self.registry.state_manager.picker_status.set_bit(PickerStatus.RollerToPos1, InputState.Inactive)
        self.registry.state_manager.picker_status.set_bit(PickerStatus.RollerToPos2, InputState.Inactive)
        self.registry.state_manager.picker_status.set_bit(PickerStatus.RollerToPos3, InputState.Inactive)
        self.registry.state_manager.picker_status.set_bit(PickerStatus.RollerToPos4, InputState.Inactive)
        self.registry.state_manager.picker_status.set_bit(PickerStatus.RollerToPos5, InputState.Inactive)
        self.registry.state_manager.picker_status.set_bit(PickerStatus.RollerToPos6, InputState.Active)

        # TODO: dunno about the ordering
        self.registry.state_manager.picker_inputs.set_bit(PickerInput.Sensor1, InputState.Active)
        self.registry.state_manager.picker_inputs.set_bit(PickerInput.Sensor2, InputState.Active)
        self.registry.state_manager.picker_inputs.set_bit(PickerInput.Sensor3, InputState.Active)
        self.registry.state_manager.picker_inputs.set_bit(PickerInput.Sensor4, InputState.Active)
        self.registry.state_manager.picker_inputs.set_bit(PickerInput.Sensor5, InputState.Active)
        self.registry.state_manager.picker_inputs.set_bit(PickerInput.Sensor6, InputState.Active)

        self.ser.write(b"T OK\r\n")
