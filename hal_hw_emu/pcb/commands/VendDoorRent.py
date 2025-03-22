from hal_hw_emu.pcb.common import AuxInput, BoardAddress, InputState, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Aux, "V")
class VendDoorRentCommand(SerialCommand):
    def run(self):
        self.logger.debug("VendDoorRent")
        self.registry.state_manager.aux_inputs.set_bit(AuxInput.VendDoorRent, InputState.Active)
        self.registry.state_manager.aux_inputs.set_bit(AuxInput.VendDoorClosed, InputState.Inactive)
        self.registry.state_manager.aux_inputs.set_bit(AuxInput.VendDoorSell, InputState.Inactive)
        self.ser.write(b"V OK\r\n")
