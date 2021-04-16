from ctypes import c_char_p

class L1CacheDataHolder():
    def __init__(self, manager):
        self.coherence00 = manager.Value(c_char_p, "I")
        self.coherence01 = manager.Value(c_char_p, "I")
        self.coherence10 = manager.Value(c_char_p, "I")
        self.coherence11 = manager.Value(c_char_p, "I")
        self.coherence20 = manager.Value(c_char_p, "I")
        self.coherence21 = manager.Value(c_char_p, "I")
        self.coherence30 = manager.Value(c_char_p, "I")
        self.coherence31 = manager.Value(c_char_p, "I")

        self.address00 = manager.Value("i", 0)
        self.address01 = manager.Value("i", 0)
        self.address10 = manager.Value("i", 0)
        self.address11 = manager.Value("i", 0)
        self.address20 = manager.Value("i", 0)
        self.address21 = manager.Value("i", 0)
        self.address30 = manager.Value("i", 0)
        self.address31 = manager.Value("i", 0)

        self.data00 = manager.Value("i", 0)
        self.data01 = manager.Value("i", 0)
        self.data10 = manager.Value("i", 0)
        self.data11 = manager.Value("i", 0)
        self.data20 = manager.Value("i", 0)
        self.data21 = manager.Value("i", 0)
        self.data30 = manager.Value("i", 0)
        self.data31 = manager.Value("i", 0)

    def getCoherence00(self):
        return self.coherence00.value

    def setCoherence00(self, coherence):
        self.coherence00.value = coherence
        return

    def getCoherence01(self):
        return self.coherence01.value

    def setCoherence01(self, coherence):
        self.coherence01.value = coherence
        return

    def getCoherence10(self):
        return self.coherence10.value

    def setCoherence10(self, coherence):
        self.coherence10.value = coherence
        return

    def getCoherence11(self):
        return self.coherence11.value

    def setCoherence11(self, coherence):
        self.coherence11.value = coherence
        return

    def getCoherence20(self):
        return self.coherence20.value

    def setCoherence20(self, coherence):
        self.coherence20.value = coherence
        return

    def getCoherence21(self):
        return self.coherence21.value

    def setCoherence21(self, coherence):
        self.coherence21.value = coherence
        return

    def getCoherence30(self):
        return self.coherence30.value

    def setCoherence30(self, coherence):
        self.coherence30.value = coherence
        return

    def getCoherence31(self):
        return self.coherence31.value

    def setCoherence31(self, coherence):
        self.coherence31.value = coherence
        return

    def getAddress00(self):
        return self.address00.value

    def setAddress00(self, address):
        self.address00.value = address
        return

    def getAddress01(self):
        return self.address01.value

    def setAddress01(self, address):
        self.address01.value = address
        return

    def getAddress10(self):
        return self.address10.value

    def setAddress10(self, address):
        self.address10.value = address
        return

    def getAddress11(self):
        return self.address11.value

    def setAddress11(self, address):
        self.address11.value = address
        return

    def getAddress20(self):
        return self.address20.value

    def setAddress20(self, address):
        self.address20.value = address
        return

    def getAddress21(self):
        return self.address21.value

    def setAddress21(self, address):
        self.address21.value = address
        return

    def getAddress30(self):
        return self.address30.value

    def setAddress30(self, address):
        self.address30.value = address
        return

    def getAddress31(self):
        return self.address31.value

    def setAddress31(self, address):
        self.address31.value = address
        return

    def getData00(self):
        return self.data00.value

    def setData00(self, data):
        self.data00.value = data
        return

    def getData01(self):
        return self.data01.value

    def setData01(self, data):
        self.data01.value = data
        return

    def getData10(self):
        return self.data10.value

    def setData10(self, data):
        self.data10.value = data
        return

    def getData11(self):
        return self.data11.value

    def setData11(self, data):
        self.data11.value = data
        return

    def getData20(self):
        return self.data20.value

    def setData20(self, data):
        self.data20.value = data
        return

    def getData21(self):
        return self.data21.value

    def setData21(self, data):
        self.data21.value = data
        return

    def getData30(self):
        return self.data30.value

    def setData30(self, data):
        self.data30.value = data
        return

    def getData31(self):
        return self.data31.value

    def setData31(self, data):
        self.data31.value = data
        return