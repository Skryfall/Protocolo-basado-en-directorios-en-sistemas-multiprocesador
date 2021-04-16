class Block:
    def __init__(self, number, data):
        self.number = number
        self.data = data

    def getNumber(self):
        return self.number.value

    def setNumber(self, number):
        self.number.value = number

    def getData(self):
        return self.data.value

    def setData(self, data):
        self.data.value = data