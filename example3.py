class english:
    def greatings(self):
        print("HELLO WORLD")

class sinhala:
    def greatings(self):
        print("KOHOMADA LOKE")

class language:
    def printit(self,say):
        say.greatings()


obj1 = language()
say = english()
obj1.printit(say)
