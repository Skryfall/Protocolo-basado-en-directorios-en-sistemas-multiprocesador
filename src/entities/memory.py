import block as bl
from threading import Lock, Thread

class MemorySingleton(type):
    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class Memory(metaclass=MemorySingleton):
    def __init__(self):
        self.block0 = bl.Block(0, 0)
        self.block1 = bl.Block(1, 0)
        self.block2 = bl.Block(2, 0)
        self.block3 = bl.Block(3, 0)
        self.block4 = bl.Block(4, 0)
        self.block5 = bl.Block(5, 0)
        self.block6 = bl.Block(6, 0)
        self.block7 = bl.Block(7, 0)
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

    def getBlockByNumber(self, number):
        return self.blocksDictionary.get(number)