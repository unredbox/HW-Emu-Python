from typing import Generic, TypeVar

from hal_hw_emu.pcb.common import BitString, InputState

T = TypeVar("T")


class State(BitString, Generic[T]):
    def __init__(self, size: int, bits=None):
        super().__init__(size, bits)

    @classmethod
    def from_bitstring(cls, bitstring: BitString):
        return cls(bitstring.size, bitstring.bits)

    def set_bit(self, bit: T, state: InputState):
        self.bits[bit.value] = state.value

    def get_bit(self, bit: T):
        return self.bits[bit.value]

    def is_bit_set(self, bit: T):
        return self.bits[bit.value] == InputState.Active.value
