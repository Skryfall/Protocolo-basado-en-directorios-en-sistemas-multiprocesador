class Block:
    def __init__(self, number, data):
        self.number = number
        self.data = data

    def getNumber(self):
        return self.number

    def setNumber(self, number):
        self.number = number

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data