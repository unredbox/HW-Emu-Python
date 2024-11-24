from abc import ABCMeta, abstractmethod
from logging import Logger

from serial import Serial

from hal_hw_emu.pcb.common import BoardAddress


class SerialCommand(metaclass=ABCMeta):
    """
    Base class for serial commands
    """

    address: BoardAddress
    code: str
    ser: Serial
    logger: Logger

    def __init__(self, ser: Serial, logger: Logger):
        self.ser = ser
        self.logger = logger

    @abstractmethod
    def run(self, **kwargs):
        raise NotImplementedError
