import serial
import time

baudrate = 9600
com = 'COM3'
receiver = serial.Serial(com, baudrate)
time.sleep(2)
receiver.readline()

val = 100 # ここの値を変更すると、Arduinoの挙動が変わる
# a = str(val) + 'a'
# receiver.write(bytes(a,'utf-8'))

while True:
    val_arduino = receiver.readline()
    val_decoded = int(repr(val_arduino.decode())[1:-5])
    print(val_decoded)
    s = input('If input q key, close this port.\n')
    if(s == 'q'):
        break
receiver.close()