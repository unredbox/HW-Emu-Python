from enum import Enum

import serial

# you can change this, but make sure you have COM1 loop into it using a tool like com0com
PORT = "COM10"

READ_BUFFER_SIZE = 4096
READ_TERMINATOR = b"\r"
WRITE_TERMINATOR = b"\r\n"

CURRENT_ADDRESS = None
PICKER_INPUTS = [1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
AUX_SENSORS = [1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
PICKER_STATUS = [0] * 20  # I think this is used to track when movement is completed?
AUX_STATUS = [0] * 20  # I think this is used to track when movement is completed?

ser: serial.Serial = None


def connect():
    """
    Creates the serial connection
    """
    global ser
    ser = serial.Serial(
        port=PORT,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0,
    )

    print(f"Connected to: {ser.portstr}")


def get_bitstring(bits):
    """
    The serial connection needs to send the bits as a string of 1s and 0s, this converts the list of bits to a string
    """
    bit_string = "".join(str(bit) for bit in bits)
    return f"{bit_string[:16]} {bit_string[16:]}R"


# def send_response(data: str):
#     res = data.encode("utf8") + b"\r\n"
#     print(f"<- {data}")
#     ser.write(res)


# def process_address(data: str):
#     global ADDRESS
#     ADDRESS = data

#     send_response("OK")


# def process_picker_command(cmd: str):
#     if cmd == "O1":
#         print("SensorBarOn")
#         send_response("OK")
#     elif cmd == "P2":
#         print("SensorBarOff")
#         send_response("OK")
#     elif cmd == "J4":
#         print("RollerIn")
#         send_response("OK")
#     elif cmd == "I4":
#         print("RollerOut")
#         send_response("OK")
#     elif cmd == "K4":
#         print("RollerStop")
#         send_response("OK")
#     elif cmd == "U1":
#         # status bit 18
#         print("RollerToPos1")
#         send_response("OK")
#     elif cmd == "U2":
#         # status bit 19
#         print("RollerToPos2")
#         send_response("OK")
#     elif cmd == "U3":
#         # status bit 20
#         print("RollerToPos3")
#         send_response("OK")
#     elif cmd == "T4":
#         # status bit 15
#         print("RollerToPos4")
#         send_response("OK")
#     elif cmd == "T5":
#         # status bit 16
#         print("RollerToPos5")
#         send_response("OK")
#     elif cmd == "T6":
#         # status bit 17
#         print("RollerToPos6")
#         send_response("OK")
#     elif cmd == "O4":
#         print("FraudSensorEnablePowerTransistor")
#         send_response("OK")
#     elif cmd == "P4":
#         print("FraudSensorDisablePowerTransistor")
#         send_response("OK")
#     elif cmd == "O3":
#         print("FraudSensorEnableTransistor")
#         send_response("OK")
#     elif cmd == "P3":
#         print("FraudSensorDisableTransistor")
#         send_response("OK")
#     elif cmd == "O2":
#         print("RightlightOn")
#         send_response("OK")
#     elif cmd == "P2":
#         print("RightlightOff")
#         send_response("OK")
#     elif cmd == "O1":
#         print("Junction4On")
#         send_response("OK")
#     elif cmd == "P1":
#         print("Junction4Off")
#         send_response("OK")
#     elif cmd == "R":
#         print("ReadPickerInputs")
#         send_response(get_bitstring(PICKER_INPUTS) + "\rOK")
#     elif cmd == "K1":
#         print("GripperExtendHalt")
#         send_response("OK")
#     elif cmd == "I1":
#         print("ExtendGripperArmForTime")
#         send_response("OK")
#     elif cmd == "L1":
#         print("GripperExtend")
#         # status bit 5
#         send_response("OK")
#     elif cmd == "M1":
#         print("GripperRetract")
#         # status bit 6
#         send_response("OK")
#     elif cmd == "M3":
#         print("GripperOpen")
#         # status bit 10
#         send_response("OK")
#     elif cmd == "V":
#         print("GripperRent")
#         # status bit 12
#         send_response("OK")
#     elif cmd == "L3":
#         print("GripperClose")
#         # status bit 9
#         send_response("OK")
#     elif cmd == "M2":
#         print("TrackOpen")
#         # status bit 8
#         send_response("OK")
#     elif cmd == "L2":
#         print("TrackClose")
#         # status bit 7
#         send_response("OK")
#     elif cmd == "W":
#         print("Version001")
#         send_response("OK\r0.0.1")
#     elif cmd == "S":
#         print("Status001")
#         send_response(get_bitstring(PICKER_STATUS) + "\rOK")
#     else:
#         print("Unknown picker command")


# def process_aux_command(cmd: str):
#     if cmd == "M1":
#         print("QlmEngage")
#         send_response("OK")
#     elif cmd == "L1":
#         print("QlmDisengage")
#         send_response("OK")
#     elif cmd == "K1":
#         print("QlmHalt")
#         send_response("OK")
#     elif cmd == "P2":
#         print("QlmDoorLock")
#         send_response("OK")
#     elif cmd == "O2":
#         print("QlmDoorUnlock")
#         send_response("OK")
#     elif cmd == "O1":
#         print("AuxSensorsOn")
#         send_response("OK")
#     elif cmd == "P1":
#         print("AuxSensorsOff")
#         send_response("OK")
#     elif cmd == "R":
#         print("AuxSensorsRead")
#         send_response(get_bitstring(AUX_SENSORS) + "\rOK")
#     elif cmd == "M2":
#         # status bit 8
#         print("VendDoorOpen")
#         send_response("OK")
#     elif cmd == "V":
#         # status bit 10
#         print("VendDoorRent")
#         send_response("OK")
#     elif cmd == "L2":
#         # status bit 7
#         print("VendDoorClose")
#         send_response("OK")
#     elif cmd == "W":
#         print("Version002")
#         send_response("0.0.1\rOK")
#     elif cmd == "S":
#         print("Status002")
#         send_response(get_bitstring(AUX_STATUS) + "\rOK")
#     elif cmd == "J2":
#         print("UnknownVendDoorCloseCommand")
#         send_response("OK")
#     elif cmd == "I2":
#         print("UnknownVendDoorOpenCommand")
#         send_response("OK")
#     elif cmd == "K2":
#         print("VendDoorKillCommand")
#         send_response("OK")
#     elif cmd == "O3":
#         print("PowerAux20")
#         send_response("OK")
#     elif cmd == "P3":
#         print("DisableAux20")
#         send_response("OK")
#     elif cmd == "O4":
#         print("PowerAux21")
#         send_response("OK")
#     elif cmd == "P4":
#         print("DisableAux21")
#         send_response("OK")
#     elif cmd == "M1":
#         print("QlmLift")
#         send_response("OK")
#     elif cmd == "L1":
#         print("QlmDrop")
#         send_response("OK")
#     else:
#         print(f"Unknown aux command: {data}")


# def process_serial_command(cmd: str):
#     if cmd == "X":
#         print("Reset")
#         send_response("OK")
#     elif cmd == "I":
#         print("AudioOn")
#         send_response("OK")
#     elif cmd == "J":
#         print("AudioOff")
#         send_response("OK")
#     elif cmd == "Y":
#         print("Version101")
#         send_response("0.0.1\rOK")
#     else:
#         print(f"Unknown serial command: {cmd}")


# def process_qr_command(cmd: str):
#     print(f"Unknown QR command: {cmd}")


# def process_command(data: str):
#     global ADDRESS

#     if ADDRESS == "H001":
#         process_picker_command(data)
#     elif ADDRESS == "H002":
#         process_aux_command(data)
#     elif ADDRESS == "H101":
#         process_serial_command(data)
#     elif ADDRESS == "H555":
#         process_qr_command(data)
#     else:
#         print(f"Unknown address: {ADDRESS}")

#     # reset
#     ADDRESS = None


def process_command(address: str, cmd: str):
    print(f"Recieved command '{cmd}' for address '{address}'")


def run():
    global CURRENT_ADDRESS

    buffer = bytearray()
    while True:
        if ser.in_waiting > 0:
            char = ser.read()
            buffer.extend(char)

            # Check if we received a full command
            if char == READ_TERMINATOR:
                if CURRENT_ADDRESS is None:
                    CURRENT_ADDRESS = buffer.rstrip(b"\r").decode("utf8")
                    # print(f"Received address selector: {CURRENT_ADDRESS}")
                    ser.write(b"OK\r\n")
                else:
                    command = buffer.rstrip(b"\r").decode("utf8")
                    process_command(CURRENT_ADDRESS, command)
                    ser.write(b"OK\r\n")
                    CURRENT_ADDRESS = None

                buffer.clear()


if __name__ == "__main__":
    connect()
    run()
