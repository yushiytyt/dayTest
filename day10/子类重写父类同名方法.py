# coding=utf-8
# class Master(object):
#     def __int__(self):
#         self.kungfu = "古法煎饼果子配方"
#
#     def make_cake(self):
#         print("[古法] 按照 <%s> 制作了一份煎饼果子..." % self.kungfu)
#
#
# class School(object):
#     def __int__(self):
#         self.kungfu = "现代煎饼果子配方"
#
#     def make_cake(self):
#         print("[现代] 按照 <%s> 制作了一份煎饼果子..." % self.kungfu)
#
#
# class Prentice(Master, School):
#     def __int__(self):
#         self.kungfu = "猫氏煎饼果子配方"
#
#     def make_cake(self):
#         self.__int__()
#         print("[猫氏] 按照 <%s> 制作了一份煎饼果子..." % self.kungfu)

#
#         # 调用父类方法格式：父类类名.父类方法(self)
#
#     def make_old_cake(self):
#         Master.__init__(self)  # 调用了父类Master的构造函数 self.kungfu = "古法...."
#         Master.make_cake(self)  # 调用了父类Master的实例方法
#
#     def make_new_cake(self):
#         School.__init__(self)  # 调用了父类School的构造函数 self.kungfu = "现代...."
#         School.make_cake(self)  # 调用父类School的实例方法


class Master(object):
    def __init__(self):
        self.kungfu = "古法煎饼果子配方"  # 实例变量，属性

    def make_cake(self):                    # 实例方法，方法
        print("[古法] 按照 <%s> 制作了一份煎饼果子..." % self.kungfu)


class School(object):
    def __init__(self):
        self.kungfu = "现代煎饼果子配方"

    def make_cake(self):
        print("[现代] 按照 <%s> 制作了一份煎饼果子..." % self.kungfu)


class Prentice(School, Master):  # 多继承，继承了多个父类
    def __init__(self):
        self.kungfu = "猫氏煎饼果子配方"

    def make_cake(self):
        self.__init__()  # 执行本类的构造函数，做属性初始化 self.kungfu = "猫氏...."
        print("[猫氏] 按照 <%s> 制作了一份煎饼果子..." % self.kungfu)

    # 调用父类方法格式：父类类名.父类方法(self)
    def make_old_cake(self):
        Master.__init__(self) # 调用了父类Master的构造函数 self.kungfu = "古法...."
        Master.make_cake(self) # 调用了父类Master的实例方法

    def make_new_cake(self):
        School.__init__(self) # 调用了父类School的构造函数 self.kungfu = "现代...."
        School.make_cake(self) # 调用父类School的实例方法，


damao = Prentice()
# 实例化对象，自动执行子类的构造函数
# def __init__(self):
#    self.kungfu = "猫氏煎饼果子配方"

print(damao.kungfu)  # 调用子类的属性（默认重写了父类的同名属性）
damao.make_cake()  # 调用子类的方法（默认重写了父类的同名方法）


damao.make_old_cake()  # 进入实例方法，再调用父类Master的方法
damao.make_new_cake()  # 进入实例方法，再调用父类School的方法

damao.make_cake()  # 调用本类的实例方法

