import entities.l1block as l1bl
#import l1block as l1bl

class L1Cache:
    def __init__(self):
        self.l1block0 = l1bl.L1Block(0, 0, 0, "I", 0)
        self.l1block1 = l1bl.L1Block(1, 0, 1, "I", 0)
        self.l1BlocksDictionary = {
                                    0: self.l1block0,
                                    1: self.l1block1
                                  }

    def getAllBlocks(self):
        return [self.l1block0, self.l1block1]

    def getL1BlockBySet(self, number):
        return self.l1BlocksDictionary.get(number)