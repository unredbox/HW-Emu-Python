from enum import Enum
from logging import Logger

from serial import Serial


class AuxInputs(Enum):
    QlmDown = 0
    QlmUp = 1
    VendDoorClosed = 2
    VendDoorSell = 3
    VendDoorRent = 4
    QlmBayDoor = 5
    Unused1 = 6
    QlmPresence = 7
    UpperExternalVend = 7
    LowerExternalVend = 8
    Unused2 = 9
    Unused3 = 10
    Unused4 = 11
    Unused5 = 12
    Unused6 = 13
    Unused7 = 14
    Unused8 = 15
    Unused9 = 16
    Unused10 = 17
    Unused11 = 18


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


class CommandRegistry:
    commands = {BoardAddress.Picker: {}, BoardAddress.Aux: {}, BoardAddress.Serial: {}, BoardAddress.QR: {}}
    ser: Serial
    logger: Logger

    def __init__(self, ser: Serial, logger: Logger):
        self.ser = ser
        self.logger = logger

    def register(self, command):
        self.commands[command.address][command.code] = command(self.ser, self.logger)
        self.logger.debug(f"Registered command {command.code} for {command.address}")

    def get_command(self, address: BoardAddress, cmd: str):
        if not address in self.commands:
            raise Exception(f"No commands registered for address")
        if not cmd in self.commands[address]:
            raise Exception(f"Unknown Command")
        return self.commands[address][cmd]
