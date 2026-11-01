import serial
import serial.tools.list_ports

port = None
ARDUINO_VID = 0x2341

for p in serial.tools.list_ports.comports():
    print(p.device, "|", p.description, "|", p.vid, p.pid)
    if p.vid == ARDUINO_VID:
        port = serial.Serial(p.device)
        break

print("waiting for data")
print(port.read())

# # shoulder 1 and 2 are 1 servo each
# # wrist1's AoR is parallel with elbow AoR
# # wrist2's AoR is perp to elbow AoR
# joint_names = ["shoulder1", "shoulder2", "elbow", "wrist1", "wrist2", "gripper"]
# joint_targets = [0, 0, 0, 0, 0] 


# def reset_to_home():
#     joint_targets = [0, 0, 0, 0, 0]


# reset_to_home()


# while True:
#     print("help for full command list")
#     cmd = input(">")

#     if (cmd == "help"):
#         print("stop, t <angle>, s <angle>, e <angle>, w1 <angle>, w2 <angle>, g")
#     elif cmd == "stop":
#         break
#     else:
#         data = cmd.split()
#         if len(data) != 2:
#             print("invalid command")
#         else :
#             try:
#                 angle = float(data[1])
#                 # elif data[0] == "t":
#                 #     pass
#                 # elif data[0] == "s":
#                 #     pass
#                 # elif data[0] == "e":
#                 #     pass
#                 # elif data[0] == "w1":
#                 #     pass
#                 # elif data[0] == "w2":
#                 #     pass
#                 # elif data[0] == "g":
#                 #     pass
#                 # else:
#                 #     print("invalid command")
#             except ValueError:
#                 print("second arg has to be numeric")