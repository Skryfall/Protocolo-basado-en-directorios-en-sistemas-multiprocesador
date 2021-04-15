import entities.block as bl
#import block as bl

class L1Block(bl.Block):
    def __init__(self, number, data, l1set, coherence, address):
        bl.Block.__init__(self, number, data)
        self.set = l1set
        self.coherence = coherence
        self.address = address

    def getSet(self):
        return self.set

    def setSet(self, l1set):
        self.l1set = l1set
        return

    def getCoherence(self):
        return self.coherence

    def setCoherence(self, coherence):
        self.coherence = coherence
        return

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address
        return