import importlib
import os
from inspect import isabstract, isclass

import serial

from commands.SerialCommand import SerialCommand
from common import AuxInputs, BitString, BoardAddress, CommandRegistry, PickerInputs, is_valid_address


class PCBEmu:
    PORT = "COM10"
    READ_TERMINATOR = b"\r"
    WRITE_TERMINATOR = b"\r\n"
    current_address = None
    PICKER_INPUTS = BitString(20)
    AUX_SENSORS = BitString(20)
    PICKER_STATUS = BitString(20)  # I think this is used to track when movement is completed?
    AUX_STATUS = BitString(20)  # I think this is used to track when movement is completed?

    ser: serial.Serial = None
    registry: CommandRegistry

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

        self.registry = CommandRegistry(self.ser)

        print(f"Connected to: {self.ser.portstr}")

    def load_commands(self):
        commands_dir = os.path.dirname(__file__) + "/commands"

        for filename in os.listdir(commands_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = f"commands.{filename[:-3]}"

                module = importlib.import_module(module_name)

                for attr_name in dir(module):
                    attr_value = getattr(module, attr_name)

                    if isclass(attr_value) and issubclass(attr_value, SerialCommand) and not isabstract(attr_value):
                        self.registry.register(attr_value)

    def process_command(self, address: str, cmd: str):
        # check if the address is a valid address
        if not is_valid_address(address):
            print(f"Unknown Address: {address}")
            self.ser.write(b"ERR\r\n")
            return

        try:
            address = BoardAddress(address)
            command = self.registry.get_command(address, cmd)

            # print(f"Running command {cmd} for {address}")
            command.run()
        except Exception as e:
            print(f"Exception running command '{cmd}' for address '{address}': {e}")
            self.ser.write(b"ERR\r\n")

    def run(self):
        buffer = bytearray()
        while True:
            if self.ser.in_waiting > 0:
                char = self.ser.read()
                buffer.extend(char)

                if char == self.READ_TERMINATOR:
                    if self.current_address is None:
                        self.current_address = buffer.rstrip(b"\r").decode("utf8")
                        self.ser.write(b"OK\r\n")
                    else:
                        command = buffer.rstrip(b"\r").decode("utf8")
                        self.process_command(self.current_address, command)
                        self.ser.write(b"OK\r\n")
                        self.current_address = None

                    buffer.clear()


if __name__ == "__main__":
    pcb = PCBEmu()
    pcb.connect()
    pcb.load_commands()
    pcb.run()
