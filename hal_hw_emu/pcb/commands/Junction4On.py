from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand

# This seems to be the same as SensorBarOn
# @serial_command(BoardAddress.Picker, "O1")
# class Junction4OnCommand(SerialCommand):
#     def run(self):
#         self.logger.debug("Junction4On")
#         self.ser.write(b"OK\r\n")
