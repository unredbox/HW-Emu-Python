from logging import Logger

from serial import Serial

from hal_hw_emu.pcb.common import BoardAddress
from hal_hw_emu.pcb.StateManager import StateManager


class CommandRegistry:
    commands = {BoardAddress.Picker: {}, BoardAddress.Aux: {}, BoardAddress.Serial: {}, BoardAddress.QR: {}}
    ser: Serial
    logger: Logger
    state_manager: StateManager

    def __init__(self, ser: Serial, logger: Logger, state_manager: StateManager):
        self.ser = ser
        self.logger = logger
        self.state_manager = state_manager

    def register(self, command):
        self.commands[command.address][command.code] = command(self)
        self.logger.debug(f"Registered command {command.code} for {command.address}")

    def get_command(self, address: BoardAddress, cmd: str):
        if not address in self.commands:
            raise Exception(f"No commands registered for address")
        if not cmd in self.commands[address]:
            raise Exception(f"Unknown Command")
        return self.commands[address][cmd]
