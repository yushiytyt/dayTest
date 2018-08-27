# """
#     列表的深拷贝和浅拷贝
#     浅拷贝：只是增加了一个数据的引用，任何引用修改数据，
#     深拷贝：
# """
# import random
#
# offices = [[], [], []]
# names = ["A", "B", "C", "D", "E", "F", "G", "H"]
# for name in names:
#     index = random.randint(0, 2)
#     offices[index].append(name)
# print(offices)
# i = 1
# for tempName in offices:
#     print("办公室%d人数：%d人" % (i, len(tempName)))
#     i += 1
#     # print(tempName)
# # print(type(tempName))
#     for name in tempName:
#         print("%s " % name, end="")
#     print()
#     print("-"*20)
#
#     # print(offices)
#     # print(name)
# #     print(index)
# # print(offices)
# # i = 1
# # for tempNames in offices:
# #     print("办公室人数为：%d" % (i, len(tempNames)))
# #     i += 1
# """
# 1、列表的合并：相加
#
# """
# list_one = [10, 20, 30, 30, 40]
# list_two = [10, 50, 60]
# list_three = list_one + list_two
# print(list_three)
# list_three.sort()  # sort排序，没有返回值的
# print(list_three)
# """
# 2、字符串转列表
#
# """
# mystrt = "hello world hello python"
# str_list = mystrt.split(" ")
# # print(str_list)
# print(list(mystrt))
# # 列表转字符串
# print(str_list)
# print(" ".join(str_list))
# # "分割符 ".join(列表参数)：默认只能转全是字符串的列表，，转成字符串
# # 其他类型的列表转字符串
# num_list = [10, 20, 30]
# print(num_list)
# numstr_list = [str(i) for i in num_list]
# print(numstr_list)
# num_str = " ".join(numstr_list)
# print(num_list)

# print("".join([str(num) for num in num_list]))
# # 3、类型判断：isinstance():可以判断是否是指定的类型，是返回True
# while True:
#     # password = input("请输入密码:")
#     if isinstance(password, str):
#         print("password是字符串")
#     else:
#         print(type(password))

# num_list1 = [12, 10, [10, 30, [100, 300, 600]], 40, [20, 40, 60, 90], 100]
# for i in num_list1:
#     if isinstance(i, list):
#         for num in i:
#             print(num)
#     else:
#         print(i)
#4、enumerate(list, tuple^)获取列表的元素和元素下标：


list_one = [10, 20, 30, 30, 40]
# enumerate(list_one)
for index, value in enumerate(list_one):
    print(index, value)