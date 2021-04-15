import entities.block as bl
#import block as bl

class L2Block(bl.Block):
    def __init__(self, number, data, coherence, owner, sharers, address):
        bl.Block.__init__(self, number, data)
        self.coherence = coherence
        self.owner = owner
        self.sharers = sharers
        self.address = address

    def getCoherence(self):
        return self.coherence

    def setCoherence(self, coherence):
        self.coherence = coherence
        return

    def getOwner(self):
        return self.owner

    def setOwner(self, owner):
        self.owner = owner
        return

    def getSharers(self):
        return self.sharers

    def setSharers(self, sharers):
        self.sharers = sharers
        return

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address
        return