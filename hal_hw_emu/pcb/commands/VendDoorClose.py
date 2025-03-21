from hal_hw_emu.pcb.common import AuxInput, BoardAddress, InputState, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Aux, "L2")
class VendDoorCloseCommand(SerialCommand):
    def run(self):
        self.logger.debug("VendDoorClose")
        self.registry.state.set_aux_input_state(AuxInput.VendDoorRent, InputState.Inactive)
        self.registry.state.set_aux_input_state(AuxInput.VendDoorSell, InputState.Inactive)
        self.registry.state.set_aux_input_state(AuxInput.VendDoorClosed, InputState.Active)
        self.ser.write(b"L OK\r\n")
