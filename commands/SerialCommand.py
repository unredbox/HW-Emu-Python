from abc import ABCMeta, abstractmethod

from serial import Serial

from common import BoardAddress


class SerialCommand(metaclass=ABCMeta):
    """
    Base class for serial commands
    """

    address: BoardAddress
    code: str
    ser: Serial

    def __init__(self, ser: Serial):
        self.ser = ser

    @abstractmethod
    def run(self, **kwargs):
        raise NotImplementedError
