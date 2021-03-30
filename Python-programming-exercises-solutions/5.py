class InputOutputString():
    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

strObj = InputOutputString()
strObj.getString()
strObj.printString()