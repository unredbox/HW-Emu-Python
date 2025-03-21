from enum import Enum


class InputState(Enum):
    Inactive = 0
    Active = 1


class AuxInput(Enum):
    QlmDown = 0
    QlmUp = 1
    VendDoorClosed = 2
    VendDoorSell = 3
    VendDoorRent = 4
    QlmBayDoor = 5
    Unused1 = 6
    QlmPresence = 7
    UpperExternalVend = 8
    LowerExternalVend = 9
    Unused2 = 10
    Unused3 = 11
    Unused4 = 12
    Unused5 = 13
    Unused6 = 14
    Unused7 = 15
    Unused8 = 16
    Unused9 = 17
    Unused10 = 18
    Unused11 = 19


class PickerInputs(Enum):
    Extend = 0
    Retract = 1
    TrackClose = 2
    TrackOpen = 3
    FingerClose = 4
    FingerSell = 5
    FingerRent = 6
    Unused1 = 7
    Unused2 = 8
    Sensor6 = 9
    Sensor4 = 10
    Sensor2 = 11
    Unused3 = 12
    Sensor1 = 13
    Sensor5 = 14
    Sensor3 = 15
    Unused4 = 16
    Unused5 = 17
    Unused6 = 18
    Unused7 = 19


class BoardAddress(Enum):
    Picker = "H001"
    Aux = "H002"
    Serial = "H101"
    QR = "H555"


def is_valid_address(value: str) -> bool:
    return any(value == item.value for item in BoardAddress)


class BitString:
    bits: list[int]

    def __init__(self, size: int, bits: list[int] = None):
        if bits:
            self.bits = bits
        else:
            self.bits = [0] * size

    def __str__(self):
        """
        The serial connection needs to send the bits as a string of 1s and 0s, this converts the list of bits to a string
        """
        bit_string = "".join(str(bit) for bit in self.bits)
        return f"{bit_string[:16]} {bit_string[16:]}R"


def serial_command(address, code):
    def decorator(cls):
        # Modify the class to set the address and code
        cls.address = address
        cls.code = code
        return cls

    return decorator
