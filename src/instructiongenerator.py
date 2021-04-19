import numpy as np

class InstructionGenerator:
    def __init__(self):
        self.generator = np.random.default_rng()

    def generateInstructionForProcessor(self):
        processor = round(self.generator.uniform(0, 3))
        instructionType = round(self.generator.uniform(0, 2))
        if (instructionType == 0):
            instruction = self.generateCalc(processor, False)
        address = round(self.generator.uniform(0, 7))
        if (instructionType == 1):
            instruction = self.generateRead(processor, address, False)
        if (instructionType == 2):
            data = round(self.generator.uniform(0, 65535))
            instruction = self.generateWrite(processor, address, data, False)
        return instruction

    def generateInstructionFromProcessor(self, processor):
        instructionType = round(self.generator.uniform(0, 2))
        if (instructionType == 0):
            instruction = self.generateCalc(processor, True)
        address = round(self.generator.uniform(0, 7))
        if (instructionType == 1):
            instruction = self.generateRead(processor, address, True)
        if (instructionType == 2):
            data = round(self.generator.uniform(0, 65535))
            instruction = self.generateWrite(processor, address, data, True)
        return instruction

    def generateCalc(self, processor, source):
        if not (source):
            return "p" + str(processor) + ": calc"
        else:
            return "calc"

    def generateRead(self, processor, address, source):
        address = self.decimalToBinary(address)
        if not (source):
            return "p" + str(processor) + ": read " + address
        else:
            return "read " + address

    def generateWrite(self, processor, address, data, source):
        address = self.decimalToBinary(address)
        data = self.decimalToHexadecimal(data)
        if not (source):
            return "p" + str(processor) + ": write " + address + ";" + data
        else:
            return "write " + address + ";" + data

    def decimalToBinary(self, decimalNumber):
        result = bin(decimalNumber).replace("0b", "")
        resultLen = len(result)
        while (resultLen != 3):
            result = "0" + result
            resultLen += 1

        return result

    def decimalToHexadecimal(self, hexadecimalNumber):
        result = hex(hexadecimalNumber).replace("0x", "")
        resultLen = len(result)
        while (resultLen != 4):
            result = "0" + result
            resultLen += 1

        return result