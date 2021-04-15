import entities.l22wayset as l2set
#import l22wayset as l2set

class L2CacheSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class L2Cache(metaclass=L2CacheSingleton):
    def __init__(self):
        self.set0 = l2set.L22WaySet(0, 1, 0)
        self.set1 = l2set.L22WaySet(2, 3, 1)
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