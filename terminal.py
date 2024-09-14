import time

is_terminal_running = True

while is_terminal_running:

    usrIn = input("Mino~$ ")
    print(usrIn)
    commands = usrIn.split(" ")

    if "sudo" in commands:
        print("No Superuser binary detected. \nAre you rooted?")

    elif "apt" in commands and "install" in commands:
        if len(commands) > 2:
            pkgname = commands[2]
            print("Reading package lists... Done")
            time.sleep(0.2)
            print("Building dependency tree... Done")
            time.sleep(0.2)
            print("Reading state information... Done")
            time.sleep(0.2)
            print("E: unable to locate the package", pkgname)
        else:
            print("Error: Missing package name")