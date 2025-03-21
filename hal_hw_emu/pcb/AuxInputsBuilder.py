from typing import Union

from hal_hw_emu.pcb.common import BitString, InputState


class AuxInputsBuilder:
    @staticmethod
    def forceInt(value: Union[int, InputState]):
        if isinstance(value, InputState):
            return value.value
        return value

    @staticmethod
    def build(
        qlm_down: Union[int, InputState],
        qlm_up: Union[int, InputState],
        vend_door_closed: Union[int, InputState],
        vend_door_sell: Union[int, InputState],
        vend_door_rent: Union[int, InputState],
        qlm_bay_door: Union[int, InputState],
        unused1: Union[int, InputState],
        qlm_presence: Union[int, InputState],
        upper_external_vend: Union[int, InputState],
        lower_external_vend: Union[int, InputState],
        unused2: Union[int, InputState] = 0,
        unused3: Union[int, InputState] = 0,
        unused4: Union[int, InputState] = 0,
        unused5: Union[int, InputState] = 0,
        unused6: Union[int, InputState] = 0,
        unused7: Union[int, InputState] = 0,
        unused8: Union[int, InputState] = 0,
        unused9: Union[int, InputState] = 0,
        unused10: Union[int, InputState] = 0,
        unused11: Union[int, InputState] = 0,
    ):
        bitstring = BitString(
            20,
            [
                AuxInputsBuilder.forceInt(qlm_down),
                AuxInputsBuilder.forceInt(qlm_up),
                AuxInputsBuilder.forceInt(vend_door_closed),
                AuxInputsBuilder.forceInt(vend_door_sell),
                AuxInputsBuilder.forceInt(vend_door_rent),
                AuxInputsBuilder.forceInt(qlm_bay_door),
                AuxInputsBuilder.forceInt(unused1),
                AuxInputsBuilder.forceInt(qlm_presence),
                AuxInputsBuilder.forceInt(upper_external_vend),
                AuxInputsBuilder.forceInt(lower_external_vend),
                AuxInputsBuilder.forceInt(unused2),
                AuxInputsBuilder.forceInt(unused3),
                AuxInputsBuilder.forceInt(unused4),
                AuxInputsBuilder.forceInt(unused5),
                AuxInputsBuilder.forceInt(unused6),
                AuxInputsBuilder.forceInt(unused7),
                AuxInputsBuilder.forceInt(unused8),
                AuxInputsBuilder.forceInt(unused9),
                AuxInputsBuilder.forceInt(unused10),
                AuxInputsBuilder.forceInt(unused11),
            ],
        )
        return bitstring

    @staticmethod
    def default():
        """
        Initial values for AuxInputs on a VMZ
        """
        return AuxInputsBuilder.build(
            qlm_down=InputState.Active.value,
            qlm_up=InputState.Active.value,
            vend_door_closed=InputState.Active.value,
            vend_door_sell=InputState.Inactive.value,
            vend_door_rent=InputState.Inactive.value,
            qlm_bay_door=InputState.Active.value,
            unused1=InputState.Inactive.value,
            qlm_presence=InputState.Inactive.value,
            upper_external_vend=InputState.Inactive.value,
            lower_external_vend=InputState.Inactive.value,
            unused2=InputState.Active.value,
            unused3=InputState.Active.value,
            unused4=InputState.Inactive.value,
            unused5=InputState.Inactive.value,
            unused6=InputState.Inactive.value,
            unused7=InputState.Inactive.value,
            unused8=InputState.Active.value,
            unused9=InputState.Inactive.value,
            unused10=InputState.Inactive.value,
            unused11=InputState.Inactive.value,
        )
