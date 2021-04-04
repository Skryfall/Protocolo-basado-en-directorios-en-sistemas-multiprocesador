import control as ctrl
import instructionsholder as instrHolder

import time
from threading import Thread

class Procesor:
    def __init__(self, number):
        self.number = number
        self.control = ctrl.Control()
        self.instrData = instrHolder.InstructionsHolder()

        self.getInstructionDictionary = {
                                                0: self.instrData.getInstruction0,
                                                1: self.instrData.getInstruction1,
                                                2: self.instrData.getInstruction2,
                                                3: self.instrData.getInstruction3
                                          }
        self.getInstructionReadDictionary = {
                                                0: self.instrData.getInstruction0Read,
                                                1: self.instrData.getInstruction1Read,
                                                2: self.instrData.getInstruction2Read,
                                                3: self.instrData.getInstruction3Read
                                              }
        self.setInstructionReadDictionary = {
                                                0: self.instrData.setInstruction0Read,
                                                1: self.instrData.setInstruction1Read,
                                                2: self.instrData.setInstruction2Read,
                                                3: self.instrData.setInstruction3Read
                                              }
        self.hexadecimalDictionary = {
                                        "0": 0,
                                        "1": 1,
                                        "2": 2,
                                        "3": 3,
                                        "4": 4,
                                        "5": 5,
                                        "6": 6,
                                        "7": 7,
                                        "8": 8,
                                        "9": 9,
                                        "A": 10,
                                        "B": 11,
                                        "C": 12,
                                        "D": 13,
                                        "E": 14,
                                        "F": 15
                                     }

    def getNumber(self):
        return self.number

    def setNumber(self, number):
        self.number = number
        return

    def binaryToDecimal(self, binaryNumber):
        result = 0
        exp = 0
        binaryNumber = binaryNumber[::-1]
        for digit in binaryNumber:
            result += int(digit) * (2**exp)
            exp += 1
        return result

    def hexadecimalToDecimal(self, hexadecimalNumber):
        result = 0
        exp = 0
        hexadecimalNumber = hexadecimalNumber[::-1]
        for digit in hexadecimalNumber:
            result += self.hexadecimalDictionary.get(digit) * (16**exp)
            exp += 1
        return result

    def readOperation(self):
        while (True):
            state = self.getInstructionReadDictionary.get(self.number)()
            if not (state):
                instr = self.getInstructionDictionary.get(self.number)()
                self.setInstructionReadDictionary.get(self.number)(True)
                if (instr[:5] == "WRITE"):
                    address = self.binaryToDecimal(instr[6:9])
                    data = self.hexadecimalToDecimal(instr[10:14])
                    time.sleep(2)
                    self.control.handleOperation("W", self.number, address, data)
                    time.sleep(3)
                elif (instr[:4] == "READ"):
                    address = self.binaryToDecimal(instr[5:8])
                    time.sleep(2)
                    self.control.handleOperation("R", self.number, address, -1)
                    time.sleep(3)
                elif (instr[:4] == "CALC"):
                    time.sleep(5)
                else:
                    print("Instrucción no Válida")

def procesor0(number):
    procesor0 = Procesor(number)
    procesor0.readOperation()

def procesor1(number):
    procesor1 = Procesor(number)
    instrData = instrHolder.InstructionsHolder()
    time.sleep(5)
    control1.handleOperation("R", 1, 0, -1)
    time.sleep(3)
    print(control1.handleOperation("R", 1, 0, -1))
    
    

process1 = Thread(target=procesor0, args=(0,))
process2 = Thread(target=procesor1, args=(1,))
process1.start()
#process2.start()

instrData = instrHolder.InstructionsHolder()
instrData.setInstruction0("WRITE 000;AAAA")
instrData.setInstruction0Read(False)