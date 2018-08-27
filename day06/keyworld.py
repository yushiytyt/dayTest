"""
 命名关键字参数：强制控制命名关键字参数的个数

 位置参数形式
 关键字参数形式
 默认参数
 多种参数的混合使用


 命名空间的访问
 locals（）：包含了所有局部变量的命名空间，格式是字典类型
 global（）：包含所有全局变量的命名空间，格式也是字典类型

  
"""


def person_info(*, name, age, job, sex):
    print(name, age, job, sex)


person_info(name="python", age=27, job="diver", sex="man")


# *args:接收所有位置参数，形成元组 **kwargs：接收所有关键字参数，形成字典


def num_func(a, b=10, c=20, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


# num_func(100, 200, 300, 400, 500, 600)
# 关键字参数后面必须也是关键字参数
# num_func(100, b=200, 300, 400, 500, 600)
num_func(100, b=200, c=300, d=400, e=500, f=600)


"""
函数的返回值：返回一个值，或者返回多个值

"""


def calc_function(num1, num2):
    pass  # 什么都不做，同时保障语法没有错误

