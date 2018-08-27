# coding=utf-8
# 导入模块就相当于将这个模块的代码跑了一遍

# 单例模式：不管你的类执行多少次实例化操作，对象只会创建一次

'''
class Person(object):
    _inserct = None

    def __new__(cls, *args, **kwargs):
        if cls._inserct is None: # 如果没有创建对象
            cls._inserct = super().__new__(cls)
            print("_new_")
            return cls._inserct
        else:
            return cls._inserct
        print("_new_")

    def __init__(self):
        print("_init_")


p1 = Person()
p2 = Person()
p3 = Person()
'''


