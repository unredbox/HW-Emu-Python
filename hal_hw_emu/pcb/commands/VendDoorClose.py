from hal_hw_emu.pcb.common import AuxInput, BoardAddress, InputState, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Aux, "L2")
class VendDoorCloseCommand(SerialCommand):
    def run(self):
        self.logger.debug("VendDoorClose")
        self.registry.state_manager.aux_inputs.set_bit(AuxInput.VendDoorClosed, InputState.Active)
        self.registry.state_manager.aux_inputs.set_bit(AuxInput.VendDoorRent, InputState.Inactive)
        self.registry.state_manager.aux_inputs.set_bit(AuxInput.VendDoorSell, InputState.Inactive)
        self.ser.write(b"L OK\r\n")
