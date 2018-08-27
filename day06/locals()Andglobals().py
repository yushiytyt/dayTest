"""
globals()
locals()

命名空间的查找迅速： LEGB规则：

local：局部命名空间
enclosing Function：嵌套函数的命名空间
Global：全局命名空间
Built-in：内置命名空间

1、局部命名空间：从函数调用时开始，到函数结束后（return、正常执行结束、抛出异常），
是改命名空间下的变量存活时间，函数结束后变量被回收
2、全局命名空间：从模块加载（代码执行）开始，到程序执行结束后，是全局命名空间的存活时间。
3、内置命名空间：从python解释器启动开始，到程序执行结束，是内置命名空间的存活时间。

"""
num = "globals"


def func():
    print(num)
    print(locals())  # 局部变量的值
    print(globals())  # 全局变量的值


func()
print(locals())  # 在模块内使用，则显示全局命名空间
print(globals())  # 显示全局命名空间的数据。任何地方都一样

# if __import__()
