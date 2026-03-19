import sys
import json
from pymavlink import mavutil

logfile = sys.argv[1]

mav = mavutil.mavlink_connection(logfile)

data = {
    "time": [],
    "vibe": [],
    "motor1": [],
    "motor2": [],
    "roll": [],
    "roll_des": []
}

while True:
    msg = mav.recv_match(blocking=False)
    if msg is None:
        break

    if msg.get_type() == "VIBE":
        data["vibe"].append(msg.VibeX)
        data["time"].append(msg.TimeUS)

    if msg.get_type() == "RCOU":
        data["motor1"].append(msg.C1)
        data["motor2"].append(msg.C2)

    if msg.get_type() == "ATT":
        data["roll"].append(msg.Roll)
        data["roll_des"].append(msg.DesRoll)

print(json.dumps(data))
