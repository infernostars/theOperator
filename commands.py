class Command:
    def __init__(self, cmd, helpinfo, executor):
        self.cmd = str(cmd)
        self.helpinfo = helpinfo
        self.executor = executor
    
    def runCmd(self, arguments):
        exec(f"""arguments = {arguments}\n{self.executor}""")

commands = [Command("test", "Testing command.", """print("hello, world!")""")]