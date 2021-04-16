from entities import l22wayset as l2set

class L2Cache():
    def __init__(self, manager):
        self.set0 = l2set.L22WaySet(manager.Value("i", 0), manager.Value("i", 1), manager.Value("i", 0), manager)
        self.set1 = l2set.L22WaySet(manager.Value("i", 2), manager.Value("i", 3), manager.Value("i", 1), manager)
        self.L2SetsDictionary = {
                                    0: self.set0,
                                    1: self.set1
                                }

    def getSet0(self):
        return self.set0

    def getSet1(self):
        return self.set1

    def getL2SetByNumber(self, number):
        return self.L2SetsDictionary.get(number)