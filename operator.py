from lib2to3.pgen2.token import OP
from operatorlib import Colors, clear, Operator
from commands import Command, commands
import os, keyboard

clear()

if os.name == 'nt': # Only if we are running on Windows
    from ctypes import windll
    k = windll.kernel32
    k.SetConsoleMode(k.GetStdHandle(-11), 7)

print(f"{Colors.GREEN}Welcome to theOperator version {Operator().getVersionString()}{Colors.END}")
history = []
try:
    while True:
        cmdraw = input(f"> ")
        args = cmdraw.split()
        cmd = args[0]
        history.insert(0, cmd)
        for c in commands:
            if cmd == c.cmd:
                c.runCmd(args, cmdraw)
                print(history)
except KeyboardInterrupt:
    clear()
    print(f"{Colors.RED}{Colors.BOLD}{Operator().getVersionString()} shutting down.{Colors.END}")