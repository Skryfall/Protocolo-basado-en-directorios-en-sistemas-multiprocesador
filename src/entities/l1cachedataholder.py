class L1CacheDataHolderSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class L1CacheDataHolder(metaclass=L1CacheDataHolderSingleton):
    def __init__(self):
        self.coherence00 = "I"
        self.coherence01 = "I"
        self.coherence10 = "I"
        self.coherence11 = "I"
        self.coherence20 = "I"
        self.coherence21 = "I"
        self.coherence30 = "I"
        self.coherence31 = "I"

        self.address00 = 0
        self.address01 = 0
        self.address10 = 0
        self.address11 = 0
        self.address20 = 0
        self.address21 = 0
        self.address30 = 0
        self.address31 = 0

        self.data00 = 0
        self.data01 = 0
        self.data10 = 0
        self.data11 = 0
        self.data20 = 0
        self.data21 = 0       
        self.data30 = 0
        self.data31 = 0

    def getCoherence00(self):
        return self.coherence00

    def setCoherence00(self, coherence):
        self.coherence00 = coherence
        return

    def getCoherence01(self):
        return self.coherence01

    def setCoherence01(self, coherence):
        self.coherence01 = coherence
        return

    def getCoherence10(self):
        return self.coherence10

    def setCoherence10(self, coherence):
        self.coherence10 = coherence
        return

    def getCoherence11(self):
        return self.coherence11

    def setCoherence11(self, coherence):
        self.coherence11 = coherence
        return

    def getCoherence20(self):
        return self.coherence20

    def setCoherence20(self, coherence):
        self.coherence20 = coherence
        return

    def getCoherence21(self):
        return self.coherence21

    def setCoherence21(self, coherence):
        self.coherence21 = coherence
        return

    def getCoherence30(self):
        return self.coherence30

    def setCoherence30(self, coherence):
        self.coherence30 = coherence
        return

    def getCoherence31(self):
        return self.coherence31

    def setCoherence31(self, coherence):
        self.coherence31 = coherence
        return

    def getAddress00(self):
        return self.address00

    def setAddress00(self, address):
        self.address00 = address
        return

    def getAddress01(self):
        return self.address01

    def setAddress01(self, address):
        self.address01 = address
        return

    def getAddress10(self):
        return self.address10

    def setAddress10(self, address):
        self.address10 = address
        return

    def getAddress11(self):
        return self.address11

    def setAddress11(self, address):
        self.address11 = address
        return

    def getAddress20(self):
        return self.address20

    def setAddress20(self, address):
        self.address20 = address
        return

    def getAddress21(self):
        return self.address21

    def setAddress21(self, address):
        self.address21 = address
        return

    def getAddress30(self):
        return self.address30

    def setAddress30(self, address):
        self.address30 = address
        return

    def getAddress31(self):
        return self.address31

    def setAddress31(self, address):
        self.address31 = address
        return

    def getData00(self):
        return self.data00

    def setData00(self, data):
        self.data00 = data
        return

    def getData01(self):
        return self.data01

    def setData01(self, data):
        self.data01 = data
        return

    def getData10(self):
        return self.data10

    def setData10(self, data):
        self.data10 = data
        return

    def getData11(self):
        return self.data11

    def setData11(self, data):
        self.data11 = data
        return

    def getData20(self):
        return self.data20

    def setData20(self, data):
        self.data20 = data
        return

    def getData21(self):
        return self.data21

    def setData21(self, data):
        self.data21 = data
        return

    def getData30(self):
        return self.data30

    def setData30(self, data):
        self.data30 = data
        return

    def getData31(self):
        return self.data31

    def setData31(self, data):
        self.data31 = data
        return