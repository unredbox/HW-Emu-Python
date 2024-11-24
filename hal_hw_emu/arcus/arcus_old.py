import re

import serial

PORT = "COM13"

ser = serial.Serial(
    port=PORT,
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0,
)
print("connected to: " + ser.portstr)

read_terminator = b"\r\x00"
motor_moving = True  # motor starts as moving
motor_moving_counter = 5  # number of status queries before motor stops
encoder_values = [0, 0]  # position reported by encoder
position_values = [0, 0]  # position that the motor should be at based on commands


def send_response(data: bytes):
    print(f"<- {data}")
    ser.write(data)


# this was authored by WinDVD
def get_motor_status():
    global motor_moving

    bits = [0] * 12  # initialize 12 bits for motor status

    if motor_moving:
        bits[0] = 1  # motor in acceleration (bit 0)
        bits[1] = 1  # motor in deceleration (bit 1)
        bits[2] = 1  # motor running at constant speed (bit 2)
        # bits[3] remains 0
        # other bits remain 0
    else:
        # motor is stopped
        bits[0] = 0  # motor not accelerating
        bits[1] = 0  # motor not decelerating
        bits[2] = 0  # motor not running at constant speed
        # bits[3] remains 0
        # Other bits remain 0

    # combine bits into an integer
    motor_status = 0
    for i in range(len(bits)):
        motor_status |= bits[i] << i
    return motor_status


def process(data: str):
    global motor_moving, motor_moving_counter
    i_cmd_regex = re.compile(r"I\d+")
    e_cmd_regex = re.compile(r"E(X|Y)")
    p_cmd_regex = re.compile(r"P(X|Y)")

    cmd = data
    value = None

    print(f"-> {data}")
    if "=" in data:
        cmd, value = data.split("=", 1)
    if cmd == "MSTX" or cmd == "MSTY":
        status = get_motor_status()
        send_response(f"{status}\x04".encode("ascii"))
        # simulate motor movement stopping after a few queries
        if motor_moving:
            motor_moving_counter -= 1
            print(f"[COM4] motor_moving_counter is now {motor_moving_counter}")
            if motor_moving_counter <= 0:
                motor_moving = False
                print("[COM4] Motor has stopped moving")
    elif i_cmd_regex.match(cmd):
        # xy targed move
        motor = int(cmd[1:])  # get motor number, 1-11
        if ":" in value:
            raise Exception("I command with X and Y not implemented")
        else:
            position = int(value)
            print(f"Got an I command for motor {motor} to move to {position}")

        send_response(b"OK\x04")
    elif e_cmd_regex.match(cmd):  # if the command is EY or EX (set or get)
        axis = cmd[1]
        if axis == "X":
            if value:
                encoder_values[0] = int(value)
                print(f"[COM4] Encoder X set to {encoder_values[0]}")
                send_response(b"OK\x04")
            else:
                send_response(f"{encoder_values[0]}\x04".encode("ascii"))
        elif axis == "Y":
            if value:
                encoder_values[1] = int(value)
                print(f"[COM4] Encoder Y set to {encoder_values[1]}")
                send_response(b"OK\x04")
            else:
                send_response(f"{encoder_values[1]}\x04".encode("ascii"))
        else:
            raise Exception("Invalid axis")
    elif p_cmd_regex.match(cmd):  # if the command is PX or PY (set or get)
        axis = cmd[1]
        if axis == "X":
            if value:
                position_values[0] = int(value)
                print(f"[COM4] Position X set to {position_values[0]}")
                send_response(b"OK\x04")
            else:
                send_response(f"{position_values[0]}\x04".encode("ascii"))
        elif axis == "Y":
            if value:
                position_values[1] = int(value)
                print(f"[COM4] Position Y set to {position_values[1]}")
                send_response(b"OK\x04")
            else:
                send_response(f"{position_values[1]}\x04".encode("ascii"))
        else:
            raise Exception("Invalid axis")
    elif cmd.startswith("X"):  # X move, in the format X-5000
        position = int(cmd[1:])
        position_values[0] = position
        encoder_values[0] = position
        print(f"[COM4] Position X set to {position}")
        send_response(b"OK\x04")
    elif cmd.startswith("Y"):  # Y move, in the format Y-5000
        position = int(cmd[1:])
        position_values[1] = position
        encoder_values[1] = position
        print(f"[COM4] Position Y set to {position}")
        send_response(b"OK\x04")
    else:
        send_response(b"OK\x04")


buffer = bytearray()
try:
    while True:
        data = ser.read(4096)

        if data:
            buffer.extend(data)

            if buffer.endswith(read_terminator):
                data, buffer = buffer.split(read_terminator, 1)
                try:
                    process(data.decode("utf8"))
                except Exception as e:
                    print(f"Error processing data: {e}")
                    send_response(b"ERR\x04")

                buffer.clear()
finally:
    ser.close()
