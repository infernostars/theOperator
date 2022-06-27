from operatorlib import Colors as clr
import os

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

class Command:
    def __init__(self, cmd, helpinfo, executor):
        self.cmd = str(cmd)
        self.helpinfo = helpinfo
        self.executor = executor
    
    def runCmd(self, arguments):
        exec(f"""arguments = {arguments}\n{self.executor}""")

commands = [Command("test", "Testing command.", """print("hello, world!")""")]

print(f"{clr.GREEN}Welcome to theOperator version {Operator().getVersionString()}{clr.END}")
cmdraw = input(f"> ")
args = cmdraw.split()
cmd = args[0]

for c in commands:
    if cmd == c.cmd:
        c.runCmd(args)