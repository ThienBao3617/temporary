import time
import serial.tools.list_ports

try:
    ser = serial.Serial(port = "COM12", baudrate = 9600)
    print("Open COM successfully")
except:
    print('Can not open the port')

relay1_ON = [0,6,0,0,0,255,200,91]
relay1_OFF = [0,6,0,0,0,0,136,27]

# relay2_ON = [15,6,0,0,0,255,200,164]
# relay2_OFF = [15,6,0,0,0,0,136,228]

relay3_ON = [1,6,0,0,0,255,201,138]
relay3_OFF = [1,6,0,0,0,0,89,202]

relay4_ON = [2,6,0,0,0,255,201,185]
relay4_OFF = [2,6,0,0,0,0,89,249]

relay5_ON = [3,6,0,0,0,255,200,68]
relay5_OFF = [3,6,0,0,0,0,88,28]

relay6_ON = [4,6,0,0,0,255,201,223]
relay6_OFF = [4,6,0,0,0,0,89,159]

relay7_ON = [5,6,0,0,0,255,200,14]
relay7_OFF = [5,6,0,0,0,0,88,78]

relay8_ON = [6,6,0,0,0,255,200,61]
relay8_OFF = [6,6,0,0,0,0,88,125]

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
ser.write(relay1_OFF)
time.sleep(2)
