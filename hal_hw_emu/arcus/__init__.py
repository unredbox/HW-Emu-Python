import importlib
import logging
import os
from inspect import isabstract, isclass

import serial

from hal_hw_emu.arcus.common import CommandRegistry
from hal_hw_emu.arcus.SerialCommand import SerialCommand


class Arcus:
    PORT = "COM13"
    READ_TERMINATOR = b"\r\x00"
    WRITE_TERMINATOR = b"\r\n"

    is_running = True
    ser: serial.Serial = None
    registry: CommandRegistry
    logger = logging.getLogger("Arcus")

    def connect(self):
        """
        Creates the serial connection
        """
        self.ser = serial.Serial(
            port=self.PORT,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0,
        )

        self.registry = CommandRegistry(self.ser, self.logger)

        self.logger.info(f"Connected to: {self.ser.portstr}")

    def load_commands(self):
        commands_dir = os.path.join(os.path.dirname(__file__), "commands")

        for filename in os.listdir(commands_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = f"hal_hw_emu.arcus.commands.{filename[:-3]}"

                module = importlib.import_module(module_name)

                for attr_name in dir(module):
                    attr_value = getattr(module, attr_name)

                    if isclass(attr_value) and issubclass(attr_value, SerialCommand) and not isabstract(attr_value):
                        self.registry.register(attr_value)

        self.logger.info(f"Loaded {len(self.registry.commands)} commands")

    def process_command(self, cmd: str):
        try:
            # cmd, value = (data, None)
            # # if the command is a setter, split the command and value
            # if "=" in data:
            #     cmd, value = data.split("=", 1)
            command = self.registry.get_command(cmd)
            args = self.registry.extract_args(cmd, command)

            self.logger.debug(f"Running command {cmd} with args: {args}")
            command.run(**args)
        except Exception as e:
            self.logger.error(f"Exception running command '{cmd}': {e}")
            self.ser.write(b"ERR\r\n")

    def start(self):
        self.connect()
        self.load_commands()
        self.loop()

    def loop(self):
        buffer = bytearray()
        while self.is_running:
            if self.ser.in_waiting > 0:
                char = self.ser.read()
                buffer.extend(char)

                if buffer.endswith(self.READ_TERMINATOR):
                    command = buffer.decode("utf8")
                    self.process_command(command)

                    buffer.clear()

    def stop(self):
        self.logger.info("Stop called")
        self.is_running = False
        if self.ser.is_open:
            self.ser.close()
