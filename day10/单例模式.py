# coding=utf-8
# 单例模式：一种常见的设计模式，不管类做了多少次实例化操作，都只创建一个对象，


class Person(object):
    _instance = None  # 创建实例变量保存对象
    _is_first = True

    def __new__(cls, *args, **kwargs):
        # print("_new_被调用")
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, name, age):
        # 这一块不属于单例模式内容
        if self._is_first:
            self.name = name
            self.age = age
            print(self.name, self.age)
            print("_init_被调用")
            self._is_first = False


p1 = Person("章", 25)
p2 = Person("李", 35)
p3 = Person("于", 20)
print(p1)
print(p2)
print(p3)
