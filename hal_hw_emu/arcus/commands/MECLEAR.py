from hal_hw_emu.arcus.common import serial_command
from hal_hw_emu.arcus.SerialCommand import SerialCommand


@serial_command("MECLEAR(?P<axis>X|Y|Z|U)", "MECLEAR", "Clear motor error")
class MEClearCommand(SerialCommand):
    def run(self, axis: str):
        self.logger.debug(f"MEClear; Axis {axis}")
        self.ser.write(b"\x04")
