from hal_hw_emu.pcb.AuxInputsBuilder import AuxInputsBuilder
from hal_hw_emu.pcb.common import AuxInput, AuxStatus, PickerInput, PickerStatus
from hal_hw_emu.pcb.PickerInputsBuilder import PickerInputsBuilder
from hal_hw_emu.pcb.State import State


class StateManager:
    picker_inputs: State[PickerInput]
    aux_inputs: State[AuxInput]
    picker_status: State[PickerStatus]
    aux_status: State[AuxStatus]

    def __init__(self):
        self.picker_inputs = State[PickerInput].from_bitstring(PickerInputsBuilder.default())
        self.aux_inputs = State[AuxInput].from_bitstring(AuxInputsBuilder.default())
        self.picker_status = State[PickerStatus](20)
        self.aux_status = State[AuxStatus](20)
