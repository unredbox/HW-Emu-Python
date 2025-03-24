from typing import Union

from hal_hw_emu.pcb.common import BitString, InputState


class PickerInputsBuilder:
    @staticmethod
    def forceInt(value: Union[int, InputState]):
        if isinstance(value, InputState):
            return value.value
        return value

    @staticmethod
    def build(
        extend: Union[int, InputState],
        retract: Union[int, InputState],
        track_close: Union[int, InputState],
        track_open: Union[int, InputState],
        finger_close: Union[int, InputState],
        finger_sell: Union[int, InputState],
        finger_rent: Union[int, InputState],
        unused1: Union[int, InputState],
        unused2: Union[int, InputState],
        sensor6: Union[int, InputState],
        sensor4: Union[int, InputState],
        sensor2: Union[int, InputState],
        unused3: Union[int, InputState],
        sensor1: Union[int, InputState],
        sensor5: Union[int, InputState],
        sensor3: Union[int, InputState],
        unused4: Union[int, InputState],
        unused5: Union[int, InputState],
        unused6: Union[int, InputState],
        unused7: Union[int, InputState],
    ):
        bitstring = BitString(
            20,
            [
                PickerInputsBuilder.forceInt(extend),
                PickerInputsBuilder.forceInt(retract),
                PickerInputsBuilder.forceInt(track_close),
                PickerInputsBuilder.forceInt(track_open),
                PickerInputsBuilder.forceInt(finger_close),
                PickerInputsBuilder.forceInt(finger_sell),
                PickerInputsBuilder.forceInt(finger_rent),
                PickerInputsBuilder.forceInt(unused1),
                PickerInputsBuilder.forceInt(unused2),
                PickerInputsBuilder.forceInt(sensor6),
                PickerInputsBuilder.forceInt(sensor4),
                PickerInputsBuilder.forceInt(sensor2),
                PickerInputsBuilder.forceInt(unused3),
                PickerInputsBuilder.forceInt(sensor1),
                PickerInputsBuilder.forceInt(sensor5),
                PickerInputsBuilder.forceInt(sensor3),
                PickerInputsBuilder.forceInt(unused4),
                PickerInputsBuilder.forceInt(unused5),
                PickerInputsBuilder.forceInt(unused6),
                PickerInputsBuilder.forceInt(unused7),
            ],
        )
        return bitstring

    @staticmethod
    def default():
        return PickerInputsBuilder.build(
            extend=InputState.Inactive,
            retract=InputState.Active,
            track_close=InputState.Active,
            track_open=InputState.Inactive,
            finger_close=InputState.Inactive,
            finger_sell=InputState.Inactive,
            finger_rent=InputState.Active,
            unused1=InputState.Inactive,
            unused2=InputState.Inactive,
            sensor6=InputState.Inactive,
            sensor4=InputState.Inactive,
            sensor2=InputState.Inactive,
            unused3=InputState.Inactive,
            sensor1=InputState.Inactive,
            sensor5=InputState.Inactive,
            sensor3=InputState.Inactive,
            unused4=InputState.Active,
            unused5=InputState.Inactive,
            unused6=InputState.Inactive,
            unused7=InputState.Inactive,
        )
