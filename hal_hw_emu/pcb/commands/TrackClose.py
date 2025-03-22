from hal_hw_emu.pcb.common import BoardAddress, InputState, PickerStatus, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "L2")
class TrackCloseCommand(SerialCommand):
    def run(self):
        self.logger.debug("TrackClose")
        self.registry.state_manager.picker_status.set_bit(PickerStatus.TrackClose, InputState.Active)
        self.registry.state_manager.picker_status.set_bit(PickerStatus.TrackOpen, InputState.Inactive)
        self.ser.write(b"L OK\r\n")
