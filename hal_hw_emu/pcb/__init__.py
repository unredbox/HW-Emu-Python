import importlib
import logging
import os
from inspect import isabstract, isclass

import serial

from hal_hw_emu.pcb.CommandRegistry import CommandRegistry
from hal_hw_emu.pcb.common import BoardAddress, is_valid_address
from hal_hw_emu.pcb.SerialCommand import SerialCommand
from hal_hw_emu.pcb.State import State
from hal_hw_emu.pcb.StateManager import StateManager


class PCB:
    PORT = "COM10"
    READ_TERMINATOR = b"\r"
    WRITE_TERMINATOR = b"\r\n"
    current_address = None

    is_running = True
    ser: serial.Serial = None
    registry: CommandRegistry
    logger = logging.getLogger("PCB")
    state_manager: StateManager

    def connect(self):
        """
        Creates the serial connection
        """
        self.state_manager = StateManager()
        self.ser = serial.Serial(
            port=self.PORT,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0,
        )

        self.registry = CommandRegistry(self.ser, self.logger, self.state_manager)

        self.logger.info(f"Connected to: {self.ser.portstr}")

    def load_commands(self):
        commands_dir = os.path.join(os.path.dirname(__file__), "commands")

        for filename in os.listdir(commands_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = f"hal_hw_emu.pcb.commands.{filename[:-3]}"

                module = importlib.import_module(module_name)

                for attr_name in dir(module):
                    attr_value = getattr(module, attr_name)

                    if isclass(attr_value) and issubclass(attr_value, SerialCommand) and not isabstract(attr_value):
                        self.registry.register(attr_value)

        cmd_count = sum(len(items) for items in self.registry.commands.values())
        self.logger.info(f"Loaded {cmd_count} commands")

    def process_command(self, address: str, cmd: str):
        # check if the address is a valid address
        if not is_valid_address(address):
            self.logger.error(f"Unknown Address: {address}")
            self.ser.write(b"ERR\r\n")
            return

        try:
            address = BoardAddress(address)
            command = self.registry.get_command(address, cmd)

            self.logger.debug(f"Running command {cmd} for {address}")
            command.run()
        except Exception as e:
            self.logger.error(f"Exception running command '{cmd}' for address '{address}': {e}")
            # print trace
            self.logger.exception(e)
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

                if char == self.READ_TERMINATOR:
                    if self.current_address is None:
                        self.current_address = buffer.rstrip(b"\r").decode("utf8")
                        self.ser.write(("SEL ADD {} OK\r\n".format(self.current_address[1:])).encode())
                    else:
                        command = buffer.rstrip(b"\r").decode("utf8")
                        self.process_command(self.current_address, command)
                        self.current_address = None

                    buffer.clear()

    def stop(self):
        self.logger.info("Stop called")
        self.is_running = False
        if self.ser.is_open:
            self.ser.close()
