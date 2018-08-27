# coding=gbk
import os

# 1、返回当前文件的绝对路径
# file_name = os.getcwd()
# print(file_name)

# 2、判断文件是否存在,存在返回True，不存在则返回False

# print(os.path.exists(r".\test.txt"))

# 3、删除指定路径的文件
# os.remove(r".\test.txt")

# 4、给指定文件重命名,os.rename(old_name, new_name)
# os.rename("test.txt", "test1.txt")

# 5、获取当前目录下的所有文件(默认是当前目录，可以指定目录)，返回一个列表
# file_name_list = os.listdir(r"C:\Users\Administrator\Desktop")
# f = open("pp.txt", "r", encoding="utf-8")
# print(file_name_list)
# for file_hlc in file_name_list:
#     if "pp.txt" in file_hlc:
#         # print("pp.txt".read())
#         print("aa")
#     else:
#         print("文件不存在")
# fil = open("pp.txt", "r", encoding="utf-8")
# for hlc_file in file_name_list:
#     if 'pp.txt' in hlc_file:
#         fil.close()
#         print(fil.read())
#     else:
#         print("[ERROR]")


# 6、创建一个目录文件
# os.mkdir(r"C:\Users\Administrator\Desktop", TEST)
# os.mkdir("")
# file_name = os.getcwd()
# print(file_name)
# os.mkdir(r"G:\pycode2")


# 7、在指定位置创建多级目录 r:保留里面的字符
# os.makedirs(r"")


# 8、删除指定路径一个目录

# os.rmdir(r"G:\pycode1")
# file_name = os.listdir(r"G:\A")
# print(file_name)

# 9、删除多级目录
# os.removedirs("")
