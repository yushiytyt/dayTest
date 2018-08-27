# coding=utf-8
class Person(object):
    # 保存实例对象
    _instance = None

    def __new__(cls, *args, **kwargs):  # 1、类属性：创建对象是会被调用
        print("_new_被调用")

        if cls._instance == None:  # 2、第一次创建
            # _new_返回：必须返回一个实例对象，如果对象是当前类的，则接下来调用_init_()方法
            cls._instance = super().__new__(cls)

        # return super().__new__(cls)  # 返回父类的_new_方法
        return cls._instance  # 否则

    def __init__(self):
        print("_init_被调用")


a = Person()
b = Person()
print(a)
print(b)
