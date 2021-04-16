from entities import l2block as l2bl
from ctypes import c_char_p

class L22WaySet:
    def __init__(self, number0, number1, l2set, manager):
        self.l2block0 = l2bl.L2Block(number0, manager.Value("i", 0), manager.Value(c_char_p, "DI"), manager.Value("i", -1), manager.list(), manager.Value("i", 0))
        self.l2block1 = l2bl.L2Block(number1, manager.Value("i", 0), manager.Value(c_char_p, "DI"), manager.Value("i", -1), manager.list(), manager.Value("i", 0))
        self.set = l2set
        self.L2BlocksDictionary = {
                                    0: self.l2block0,
                                    1: self.l2block1
                                  }

    def getSet(self):
        return self.set.value

    def setSet(self, l2set):
        self.set.value = l2set
        return

    def getBlock0(self):
        return self.l2block0

    def getBlock1(self):
        return self.l2block1

    def getAllBlocks(self):
        return [self.l2block0, self.l2block1]

    def getL2BlockByNumber(self, number):
        return self.L2BlocksDictionary.get(number)