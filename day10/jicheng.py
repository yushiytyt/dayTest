# coding=utf-8
class Masters1(object):
    def __int__(self):
        self.kunFu = "古法煎饼果子配方"

    def make_cake(self):
        print("按照<%s>制作了一份煎饼果子……" % self.kunFu)


class XianDai(object):
    def __int__(self):
        self.kunFu1 = "现代煎饼果子配方"

    def make_cake1(self):
        print("按照<%s>制作了一份煎饼果子……" % self.kunFu1)


class TuDi(Masters1, XianDai):
    # print("tudi")
    pass


# laoLi = Masters1()
# print(laoLi)
# print(laoLi.kunfu)
# laoLi.make_cake()

daMao = Masters1()
print(daMao)

print(daMao.kunFu)
# daMao.make_cake()

