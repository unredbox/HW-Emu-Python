import re
from logging import Logger

from serial import Serial

from hal_hw_emu.arcus import SerialCommand


def serial_command(code):
    def decorator(cls):
        cls.code = code
        return cls

    return decorator


class CommandRegistry:
    commands = {}
    ser: Serial
    logger: Logger

    def __init__(self, ser: Serial, logger: Logger):
        self.ser = ser
        self.logger = logger

    def register(self, command: SerialCommand):
        self.commands[command.code] = command(self.ser, self.logger)
        self.logger.debug(f"Registered command {command.code}")

    def get_command(self, cmd: str):
        # if not cmd in self.commands[cmd]:
        #     raise Exception(f"Unknown Command")
        # return self.commands[cmd]

        # find by matching the input again the command code using regex
        for code, command in self.commands.items():
            matches = re.match(code, cmd)
            print(code, matches)
            if matches:
                return command

        raise Exception(f"Unknown Command")

    def extract_args(self, cmd: str, command: SerialCommand):
        match = re.match(command.code, cmd)
        return match.groupdict() if match else {}
