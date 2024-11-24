from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand

# @serial_command(BoardAddress.Serial, "Y")
# class VersionSerialCommand(SerialCommand):
#     def run(self):
#         self.logger.debug("VersionSerial")
#         self.ser.write(b"0.0.1\rOK\r\n")
