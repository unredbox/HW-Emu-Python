from hal_hw_emu.pcb.common import BoardAddress, InputState, PickerInput, PickerStatus, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


# Not used?
@serial_command(BoardAddress.Picker, "U1")
class RollerToPos1Command(SerialCommand):
    def run(self):
        self.logger.debug("RollerToPos1")
        # TODO: this is probably wrong
        self.registry.state_manager.picker_status.set_bit(PickerStatus.RollerToPos1, InputState.Active)
        self.registry.state_manager.picker_status.set_bit(PickerStatus.RollerToPos2, InputState.Inactive)
        self.registry.state_manager.picker_status.set_bit(PickerStatus.RollerToPos3, InputState.Inactive)
        self.registry.state_manager.picker_status.set_bit(PickerStatus.RollerToPos4, InputState.Inactive)
        self.registry.state_manager.picker_status.set_bit(PickerStatus.RollerToPos5, InputState.Inactive)
        self.registry.state_manager.picker_status.set_bit(PickerStatus.RollerToPos6, InputState.Inactive)

        # # TODO: dunno about the ordering
        # self.registry.state_manager.picker_inputs.set_bit(PickerInput.Sensor1, InputState.Active)
        # self.registry.state_manager.picker_inputs.set_bit(PickerInput.Sensor2, InputState.Inactive)
        # self.registry.state_manager.picker_inputs.set_bit(PickerInput.Sensor3, InputState.Inactive)
        # self.registry.state_manager.picker_inputs.set_bit(PickerInput.Sensor4, InputState.Inactive)
        # self.registry.state_manager.picker_inputs.set_bit(PickerInput.Sensor5, InputState.Inactive)
        # self.registry.state_manager.picker_inputs.set_bit(PickerInput.Sensor6, InputState.Inactive)

        self.ser.write(b"U OK\r\n")
