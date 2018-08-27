"""
函数：
return:只会用在函数里，返回一个数据，同时结束函数
如果return 后面没有数据，则默认返回None，除了False、0、None也可以表示条件不成立


返回年龄大于23岁的成员姓名

输入姓名、年龄，如果小于23岁，就存入人才储备信息库


关键字参数：如果不确定参数的顺序，可以通过关键字参数形式传递数据、避免误传

默认参数：

python的参数是通过引用来传递的


默认参数使用可变数据类型

参数不能使用可变数据类型

"""

# person_info1 = []
#
#
# def person_info(name, age):
#     if age <= 23:
#         print("[INFO]:存储成功！")
#         return name
#     else:
#         print("[ERROR]:存储失败！")
#
#
# while True:
#     input_name = input("请输入姓名：")
#     input_age = int(input("请输入年龄："))
#     new_name = person_info(input_name, input_age)
#     person_info1.append(new_name)
#     # print(new_name)
#     print(person_info1)


# *args :收集所有的位置参数，合并为元组


def people_info(*args):
    print(type(args))
    print("aa")


people_info()
people_info("a")
people_info(6, 4)


# 2、**kw ：收集所有的关键字参数，合并为字典


def people_list(**kw):
    print(type(kw))


people_list()
