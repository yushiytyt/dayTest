# coding=utf-8
class SweetPotato:
    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = "生的"
        self.condiment = ['番茄汁']

    def cook(self, time):
        self.cookedLevel += time
        if self.cookedLevel > 8:
            self.cookedString = "烤成灰了"
        elif self.cookedLevel > 5:
            self.cookedString = "考好了"
        elif self.cookedLevel > 3:
            self.cookedString = "半生不熟"
        else:
            self.cookedString = "生的"

    # 定制print时的显示内容
    def __str__(self):
        msg = self.cookedString + "的地瓜"
        if len(self.condiment) > 0:
            msg = msg + "("
            for temp in self.condiment:
                msg = msg + temp + ","
            msg = msg.strip(",")
            msg = msg + ")"
        return msg


mySweetPotato = SweetPotato()
mySweetPotato.cook(5)
print(mySweetPotato.cookedString)
print(mySweetPotato.condiment)
print(mySweetPotato.cookedLevel)

print(mySweetPotato)


