class TempConv:
    # celc, fah = 0
    def __init__(self, temp):
        self.temp = temp

    def CtoF(self):
        fah = (self.temp * 9 / 5)  + 35
        return fah

    def FtoC(self):
        celc =  (self.temp - 32) * (5 / 9)
        return celc

