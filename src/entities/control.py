import l1cache as l1c
import l2cache as l2c
import memory as mem
import random

class Control:
    def __init__(self):
        self.l1cache = l1c.L1Cache()

    def handleRead(self, procNumber, address):
        if not (address % 2):
            l1block = self.l1cache.getL1BlockBySet(0)
            return self.handleReadAux(procNumber, address, l1block, 0)
        else:
            l1block = self.l1cache.getL1BlockBySet(1)
            return self.handleReadAux(procNumber, address, l1block, 1)
    
    def handleReadAux(self, procNumber, address, l1block, l2set):
        coherence = l1block.getCoherence()
        if (coherence == "I"):
            return self.handleInvalidRead(procNumber, address, l1block, l2set)
        elif (coherence == "S"):
            print("compartido")
            return
        else:
            print("modificado")
            return

    def handleInvalidRead(self, procNumber, address, l1block, l2set):
        l2cache = l2c.L2Cache()
        l2set = l2cache.getL2SetByNumber(l2set)
        l2blocks = l2set.getAllBlocks()
        for l2block in l2blocks:
            if (l2block.getCoherence() == "DI"):
                continue
            elif (l2block.getAddress() == address):
                self.setL1Block(l1block, "S", l2block.getAddress(), l2block.getData())
                self.setL2Block(l2block, "DS", l2block.getOwner(), l2block.getSharers().append(procNumber), l2block.getAddress(), l2block.getData())
               
                return

        i = random.randint(0, 1)
        l2block = l2blocks[i]
        if (l2block.getCoherence() != "DI"):
            self.setDataToMemory(l2block.getAddress(), l2block.getData())

        data = self.getDataFromMemory(address)

        self.setL2Block(l2block, "DS", procNumber, [], address, data)
        self.setL1Block(l1block, "S", address, data)
        
        return

    def getDataFromMemory(self, address):
        memory = mem.Memory()
        memblock = memory.getBlockByNumber(address)
        return memblock.getData()

    def setDataToMemory(self, address, data):
        memory = mem.Memory()
        memblock = memory.getBlockByNumber(address)
        memblock.setData(data)
        return

    def setL2Block(self, l2block, coherence, owner, sharers, address, data):
        l2block.setCoherence(coherence)
        l2block.setOwner(owner)
        l2block.setSharers(sharers)
        l2block.setAddress(address)
        l2block.setData(data)
        return

    def setL1Block(self, l1block, coherence, address, data):
        l1block.setCoherence(coherence)
        l1block.setAddress(address)
        l1block.setData(data)
        return


test = Control()

test.handleRead(2, 7)