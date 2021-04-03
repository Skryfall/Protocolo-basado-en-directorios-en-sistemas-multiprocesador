import l2block as l2bl

class L22WaySet:
    def __init__(self, number0, number1, l2set):
        self.l2block0 = l2bl.L2Block(number0, 0, "DI", 0, [], 0)
        self.l2block1 = l2bl.L2Block(number1, 0, "DI", 0, [], 0)
        self.set = l2set
        self.L2BlocksDictionary = {
                                    0: self.l2block0,
                                    1: self.l2block1
                                  }

    def getSet(self):
        return self.set

    def setSet(self, l2set):
        self.set = l2set
        return

    def getAllBlocks(self):
        return [self.l2block0, self.l2block1]

    def getL2BlockByNumber(self, number):
        return self.L2BlocksDictionary.get(number)