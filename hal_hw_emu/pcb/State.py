from hal_hw_emu.pcb.AuxInputsBuilder import AuxInputsBuilder
from hal_hw_emu.pcb.common import AuxInput, BitString, InputState


class State:
    PICKER_INPUTS = BitString(20)
    AUX_INPUTS = AuxInputsBuilder.default()  # aka Aux inputs
    PICKER_STATUS = BitString(20)  # I think this is used to track when movement is completed?
    AUX_STATUS = BitString(20)  # I think this is used to track when movement is completed?

    def set_aux_input_state(self, input: AuxInput, state: InputState):
        self.AUX_INPUTS.bits[input.value] = state.value

    def get_aux_input_state(self, input: AuxInput):
        return self.AUX_INPUTS.bits[input.value]

    def is_aux_input_active(self, input: AuxInput):
        return self.AUX_INPUTS.bits[input.value] == InputState.Active.value
