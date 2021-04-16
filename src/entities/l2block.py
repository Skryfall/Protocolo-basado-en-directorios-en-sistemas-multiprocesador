from entities import block as bl

class L2Block(bl.Block):
    def __init__(self, number, data, coherence, owner, sharers, address):
        bl.Block.__init__(self, number, data)
        self.coherence = coherence
        self.owner = owner
        self.sharers = sharers
        self.address = address

    def getCoherence(self):
        return self.coherence.value

    def setCoherence(self, coherence):
        self.coherence.value = coherence
        return

    def getOwner(self):
        return self.owner.value

    def setOwner(self, owner):
        self.owner.value = owner
        return

    def getSharers(self):
        return self.sharers

    def clearSharers(self):
        self.sharers[:] = []
        return

    def appendSharers(self, number):
        self.sharers.append(number)
        return

    def getAddress(self):
        return self.address.value

    def setAddress(self, address):
        self.address.value = address
        return