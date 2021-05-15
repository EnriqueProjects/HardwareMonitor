import serial
import time
import os
import wmi
import psutil

ser = serial.Serial('COM4', 9600)

# os.system('start D:\hardware\OpenHardwareMonitor\OpenHardwareMonitor.exe')
# os.system('runas /savecred /user:DESKTOP-DBQ6QH7\quique D:\hardware\OpenHardwareMonitor\OpenHardwareMonitor.exe')
os.system("schtasks.exe /run /tn \"mestaches\OHWsansUAC\"")
time.sleep(2)
w = wmi.WMI(namespace="root\OpenHardwareMonitor")

print("initialisation de la boucle...")

def getCpuGpu():
    cpu, gpu = 0, 0
    thermo = w.Sensor()
    for sensor in thermo:
        if sensor.SensorType == u'Temperature':
            if sensor.Name == "CPU Core":
                cpu = sensor.Value
            elif sensor.Name == "GPU Core":
                gpu = sensor.Value
    return cpu, gpu


def getMsg():
    cpu, gpu = getCpuGpu()
    cpu_usage = psutil.cpu_percent()
    msg = "CPU {}DC {}% /GPU {}DC/".format(cpu, cpu_usage, gpu)
    return msg


while(1):
    for c in getMsg():
        ser.write(c.encode())
    time.sleep(2)
