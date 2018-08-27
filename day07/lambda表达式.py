"""
lambda 表示创建一个lambda表达式
:前面是参数（如果没有参数空留）
：后面是返回值


默认参数：可变参数

：
"""

# f = lambda: 100
# print(f())
# # 1、带参数的的lambda表达式
# fun = lambda a, b: a + b


# a if a >b else b


# a if a > b else b

print(lambda a, b, c: c if c > (a if a > b else b) else (a if a > b else b)(10, 20, 30))


# 字典类型可变参数

# lambda **kwargs : {value : key for key, value in kwargs.item()}

# value : key for value, key in kwargs.item()


# 4、lambda表达式作为参数传递 :  函数作为参数传递
def func(a, b, f):
    return f(a, b)


print(func(10, 20, lambda x, y: x + y))


