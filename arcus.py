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


def process(data: str):
    print(f"-> {data}")
    # res = "?"
    # if data == "$":
    #     pass

    # send_response(res)
    ser.write(b"OK\x04")


buffer = bytearray()
try:
    while True:
        data = ser.read(4096)

        if data:
            buffer.extend(data)

            if buffer.endswith(read_terminator):
                data, buffer = buffer.split(read_terminator, 1)
                process(data.decode("utf8"))

                buffer.clear()
finally:
    ser.close()
