import time
import serial.tools.list_ports

try:
    ser = serial.Serial(port = "/dev/ttyAMA2", baudrate = 9600)
    print("Open COM successfully")
except:
    print('Can not open the port')

# relay1_ON = [0,6,0,0,0,255,200,91]
# relay1_OFF = [0,6,0,0,0,0,136,27]

# relay2_ON = [15,6,0,0,0,255,200,164]
# relay2_OFF = [15,6,0,0,0,0,136,228]

relay1_ON = [1,6,0,0,0,255,201,138]
relay1_OFF = [1,6,0,0,0,0,137,202]

relay2_ON = [2,6,0,0,0,255,201,185]
relay2_OFF = [2,6,0,0,0,0,137,249]

relay3_ON = [3,6,0,0,0,255,200,104]
relay3_OFF = [3,6,0,0,0,0,136,40]

relay4_ON = [4,6,0,0,0,255,201,223]
relay4_OFF = [4,6,0,0,0,0,137,159]

relay5_ON = [5,6,0,0,0,255,200,14]
relay5_OFF = [5,6,0,0,0,0,136,78]

relay6_ON = [6,6,0,0,0,255,200,61]
relay6_OFF = [6,6,0,0,0,0,136,125]

relay7_ON = [7,6,0,0,0,255,201,236]
relay7_OFF = [7,6,0,0,0,0,137,172]

relay8_ON = [8,6,0,0,0,255,201,19]
relay8_OFF = [8,6,0,0,0,0,137,83]

def set_device1(state):
    if state == True:
        ser.write(relay1_ON)
    else:
        ser.write(relay1_OFF)
    # time.sleep(1)
    # return serial_read_data(ser)

def set_device2(state):
    if state == True:
        ser.write(relay2_ON)
    else:
        ser.write(relay2_OFF)

def serial_read_data(ser):
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        out = ser.read(bytesToRead)
        data_array = [b for b in out]
        print(data_array)
        if len(data_array) >= 7:
            array_size = len(data_array)
            value = data_array[array_size - 4] * 256 + data_array[array_size - 3]
            return value
        else:
            return -1
    return 0

soil_temperature =[1, 3, 0, 6, 0, 1, 100, 11]
def readTemperature():
    serial_read_data(ser)
    ser.write(soil_temperature)
    time.sleep(1)
    return serial_read_data(ser)

soil_moisture = [1, 3, 0, 7, 0, 1, 53, 203]
def readMoisture():
    serial_read_data(ser)
    ser.write(soil_moisture)
    time.sleep(1)
    return serial_read_data(ser)

# while True:
#     print("TEST RELAY")
#     set_device1(True)
#     time.sleep(10)
#     set_device1(False)
#     time.sleep(10)
#     set_device2(True)
#     time.sleep(10)
#     set_device2(False)
#     time.sleep(10)
#     print("TEST SENSOR")
#     print(readMoisture())
#     time.sleep(1)
#     print(readTemperature())
#     time.sleep(1)

ser.write(relay1_ON)
time.sleep(2)
print("ON1_OK")
ser.write(relay1_OFF)
time.sleep(2)
print("OFF1_OK")

ser.write(relay2_ON)
time.sleep(2)
print("ON2_OK")
ser.write(relay2_OFF)
time.sleep(2)
print("OFF2_OK")

ser.write(relay3_ON)
time.sleep(2)
print("ON3_OK")
ser.write(relay3_OFF)
time.sleep(2)
print("OFF3_OK")

ser.write(relay4_ON)
time.sleep(2)
print("ON4_OK")
ser.write(relay4_OFF)
time.sleep(2)
print("OFF4_OK")

ser.write(relay5_ON)
time.sleep(2)
print("ON5_OK")
ser.write(relay5_OFF)
time.sleep(2)
print("OFF5_OK")

ser.write(relay6_ON)
time.sleep(2)
print("ON6_OK")
ser.write(relay6_OFF)
time.sleep(2)
print("OFF6_OK")

ser.write(relay7_ON)
time.sleep(2)
print("ON7_OK")
ser.write(relay7_OFF)
time.sleep(2)
print("OFF7_OK")

ser.write(relay8_ON)
time.sleep(2)
print("ON8_OK")
ser.write(relay8_OFF)
time.sleep(2)
print("OFF8_OK")
