from threading import Lock, Thread

class InstructionsHolderSingleton(type):
    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class InstructionsHolder(metaclass=InstructionsHolderSingleton):
    def __init__(self):
        self.instruction0 = ""
        self.instruction0Read = True
        self.instruction1 = ""
        self.instruction1Read = True
        self.instruction2 = ""
        self.instruction2Read = True
        self.instruction3 = ""
        self.instruction3Read = True

    def getInstruction0(self):
        return self.instruction0

    def setInstruction0(self, instruction):
        self.instruction0 = instruction
        return

    def getInstruction0Read(self):
        return self.instruction0Read

    def setInstruction0Read(self, state):
        self.instruction0Read = state
        return

    def getInstruction1(self):
        return self.instruction1

    def setInstruction1(self, instruction):
        self.instruction1 = instruction
        return

    def getInstruction1Read(self):
        return self.instruction1Read

    def setInstruction1Read(self, state):
        self.instruction1Read = state
        return
        
    def getInstruction2(self):
        return self.instruction2

    def setInstruction2(self, instruction):
        self.instruction2 = instruction
        return

    def getInstruction2Read(self):
        return self.instruction2Read

    def setInstruction2Read(self, state):
        self.instruction2Read = state
        return

    def getInstruction3(self):
        return self.instruction3

    def setInstruction3(self, instruction):
        self.instruction3 = instruction
        return

    def getInstruction3Read(self):
        return self.instruction3Read

    def setInstruction3Read(self, state):
        self.instruction3Read = state
        return