from entities import block as bl
from multiprocessing import Manager

class Memory():
    def __init__(self, manager):
        self.block0 = bl.Block(manager.Value("i", 0), manager.Value("i", 0))
        self.block1 = bl.Block(manager.Value("i", 1), manager.Value("i", 0))
        self.block2 = bl.Block(manager.Value("i", 2), manager.Value("i", 0))
        self.block3 = bl.Block(manager.Value("i", 3), manager.Value("i", 0))
        self.block4 = bl.Block(manager.Value("i", 4), manager.Value("i", 0))
        self.block5 = bl.Block(manager.Value("i", 5), manager.Value("i", 0))
        self.block6 = bl.Block(manager.Value("i", 6), manager.Value("i", 0))
        self.block7 = bl.Block(manager.Value("i", 7), manager.Value("i", 0))
        self.blocksDictionary = {
                                    0: self.block0,
                                    1: self.block1,
                                    2: self.block2,
                                    3: self.block3,
                                    4: self.block4,
                                    5: self.block5,
                                    6: self.block6,
                                    7: self.block7
                                }

    def getBlock0(self):
        return self.block0

    def getBlock1(self):
        return self.block1

    def getBlock2(self):
        return self.block2

    def getBlock3(self):
        return self.block3

    def getBlock4(self):
        return self.block4

    def getBlock5(self):
        return self.block5

    def getBlock6(self):
        return self.block6

    def getBlock7(self):
        return self.block7

    def getBlockByNumber(self, number):
        return self.blocksDictionary.get(number)