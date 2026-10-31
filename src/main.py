
while True:
    print("help for full command list")
    cmd = input(">")

    if (cmd == "help"):
        print("stop, t <angle>, s <angle>, e <angle>, w1 <angle>, w2 <angle>, g")
    elif cmd == "stop":
        break
    else:
        data = cmd.split()
        if len(data) != 2:
            print("invalid command")
        else :
            try:
                angle = float(data[1])
                # elif data[0] == "t":
                #     pass
                # elif data[0] == "s":
                #     pass
                # elif data[0] == "e":
                #     pass
                # elif data[0] == "w1":
                #     pass
                # elif data[0] == "w2":
                #     pass
                # elif data[0] == "g":
                #     pass
                # else:
                #     print("invalid command")
            except ValueError:
                print("second arg has to be numeric")