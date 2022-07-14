class Command:
    def __init__(self, cmd, helpinfo, executor):
        self.cmd = str(cmd)
        self.helpinfo = helpinfo
        self.executor = executor
    
    def runCmd(self, arguments, rawcmd):
        exec(f"""arguments = {arguments}\nrawcmd = "{rawcmd}"\n{self.executor}""")

commands = [Command("test", "Testing command.", """print("hello, world!")"""), Command("cat", "Gives your input back to you.", """print(" ".join(arguments[1:]))""")]