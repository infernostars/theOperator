from operatorlib import Colors, clear
from commands import Command, commands
import os

clear()

if os.name == 'nt': # Only if we are running on Windows
    from ctypes import windll
    k = windll.kernel32
    k.SetConsoleMode(k.GetStdHandle(-11), 7)

class Operator:
    major = 1
    minor = 0
    build = 2

    def getVersionString(self):
        return f"{self.major}.{self.minor} (Build {self.build})"

print(f"{Colors.GREEN}Welcome to theOperator version {Operator().getVersionString()}{Colors.END}")

while True:
    cmdraw = input(f"> ")
    args = cmdraw.split()
    cmd = args[0]

    for c in commands:
        if cmd == c.cmd:
            c.runCmd(args)