from hal_hw_emu.pcb.common import BoardAddress, serial_command
from hal_hw_emu.pcb.SerialCommand import SerialCommand


@serial_command(BoardAddress.Picker, "W")
class VersionPickerCommand(SerialCommand):
    def run(self):
        self.logger.debug("VersionPicker")
        self.ser.write(b" DAN LEIWE GRIPPER CONTROLER GET_A_MOVIE 12/19/05 ADD 001 OK\r\n")
