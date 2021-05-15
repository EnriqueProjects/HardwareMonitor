import wmi

w = wmi.WMI(namespace="root\OpenHardwareMonitor")
thermo = w.Sensor()

for sensor in thermo:
    if sensor.SensorType == u'Temperature':
        if sensor.Name == "CPU Core":
            print("CPU:", sensor.Value)
        elif sensor.Name == "GPU Core":
            print("GPU:", sensor.Value)
