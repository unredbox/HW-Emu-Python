from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand

# Same as SensorBarOff
# @serial_command(BoardAddress.Picker, "P1")
# class Junction4OffCommand(SerialCommand):
#     def run(self):
#         self.logger.debug("Junction4Off")
#         self.ser.write(b"O OK\r\n")
