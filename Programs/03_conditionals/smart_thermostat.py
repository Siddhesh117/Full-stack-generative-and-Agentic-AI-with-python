# You're building a smart thermostat alert system:
#  - If the device_status is "active"
#      - And temperature > 35 -> Warn: "High temperature alert!"
#      - Else: "Temperature normal"
#  - if device is off -> "Device is offline"

device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature normal")    
else:
    print("Device is offline")
