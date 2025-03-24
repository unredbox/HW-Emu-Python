from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Serial, "Y")
class VersionSerialCommand(SerialCommand):
    def run(self):
        self.logger.debug("VersionSerial")
        self.ser.write(b"ID101 RS232 INT DANIEL LEIWE 12/16/05 OK\r\n")
