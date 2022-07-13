import serial
import time

arduino = serial.Serial('com9',9600)
time.sleep(1)

print("입력한 위치로 회전")

def process_moter
    var = input()
    var = var.encode('utf-8')
    arduino.write(var)
    time.sleep(1)
