from hal_hw_emu.pcb.common import BoardAddress, InputState, PickerStatus, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "M2")
class TrackOpenCommand(SerialCommand):
    def run(self):
        self.logger.debug("TrackOpen")
        self.registry.state_manager.picker_status.set_bit(PickerStatus.TrackOpen, InputState.Active)
        self.registry.state_manager.picker_status.set_bit(PickerStatus.TrackClose, InputState.Inactive)
        self.ser.write(b"M OK\r\n")
