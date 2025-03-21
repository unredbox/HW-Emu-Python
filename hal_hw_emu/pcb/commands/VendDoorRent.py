from hal_hw_emu.pcb.common import AuxInput, BoardAddress, InputState, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Aux, "V")
class VendDoorRentCommand(SerialCommand):
    def run(self):
        self.logger.debug("VendDoorRent")
        self.registry.state.set_aux_input_state(AuxInput.VendDoorClosed, InputState.Inactive)
        self.registry.state.set_aux_input_state(AuxInput.VendDoorSell, InputState.Inactive)
        self.registry.state.set_aux_input_state(AuxInput.VendDoorRent, InputState.Active)
        self.ser.write(b"V OK\r\n")
