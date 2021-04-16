from ctypes import c_char_p

class InstructionsHolder():
    def __init__(self, manager):
        self.instructionTime = manager.Value("i", 6)
        self.instruction0 = manager.Value(c_char_p, "")
        self.instruction0Read = manager.Value("i", 1)
        self.instruction1 = manager.Value(c_char_p, "")
        self.instruction1Read = manager.Value("i", 1)
        self.instruction2 = manager.Value(c_char_p, "")
        self.instruction2Read = manager.Value("i", 1)
        self.instruction3 = manager.Value(c_char_p, "")
        self.instruction3Read = manager.Value("i", 1)

    def getInstructionTime(self):
        return self.instructionTime.value

    def setInstructionTime(self, time):
        self.instructionTime.value = time
        return

    def getInstruction0(self):
        return self.instruction0.value

    def setInstruction0(self, instruction):
        self.instruction0.value = instruction
        return

    def getInstruction0Read(self):
        return self.instruction0Read.value

    def setInstruction0Read(self, state):
        self.instruction0Read.value = state
        return

    def getInstruction1(self):
        return self.instruction1.value

    def setInstruction1(self, instruction):
        self.instruction1.value = instruction
        return

    def getInstruction1Read(self):
        return self.instruction1Read.value

    def setInstruction1Read(self, state):
        self.instruction1Read.value = state
        return
        
    def getInstruction2(self):
        return self.instruction2.value

    def setInstruction2(self, instruction):
        self.instruction2.value = instruction
        return

    def getInstruction2Read(self):
        return self.instruction2Read.value

    def setInstruction2Read(self, state):
        self.instruction2Read.value = state
        return

    def getInstruction3(self):
        return self.instruction3.value

    def setInstruction3(self, instruction):
        self.instruction3.value = instruction
        return

    def getInstruction3Read(self):
        return self.instruction3Read.value

    def setInstruction3Read(self, state):
        self.instruction3Read.value = state
        return