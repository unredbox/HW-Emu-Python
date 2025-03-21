from abc import ABCMeta, abstractmethod
from logging import Logger

from serial import Serial

from hal_hw_emu.pcb.CommandRegistry import CommandRegistry
from hal_hw_emu.pcb.common import BoardAddress


class SerialCommand(metaclass=ABCMeta):
    """
    Base class for serial commands
    """

    address: BoardAddress
    code: str
    registry: CommandRegistry
    ser: Serial
    logger: Logger

    def __init__(self, registry: CommandRegistry):
        self.registry = registry
        self.ser = registry.ser
        self.logger = registry.logger

    @abstractmethod
    def run(self, **kwargs):
        raise NotImplementedError
