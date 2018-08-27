"""
    文件操作
    下面f是一个文件对象，可以操作本地磁盘文件helloword.txt


    文件操作的主要三个权限
    1、r：读取文件，如果文件存在，则可以读取文件，日过文件不存在，则会倒错

    2、w：读取文件，如果文件存在，则可以写入数据（会覆盖原来的数据，如果文件不存在，则新建文件）

    3、a: 追加数据，如果文件存在，则在文件末尾追加数据，如果文件不存在，则新建文件。
"""

# # 打开文件
# f = open("SMS.py", "a", encoding="utf-8")
# # 编辑文件
# f.write("追加文件")
# # 读取文件
# file = f.read()
# # 关闭文件
# print(file)
# f.close()




 #  1、打开文件， 并制定文件操作权限
# f = open("test.txt", "w")
#
# # wirte():表示向文件里写入字符串2、
# f.write("外部写入文件，测试成功")
#
# # 3、关闭文件，表示清空缓冲区的数据，并写入到磁盘文件里
# f.close()

# 编码字符集：gbk：包含了所有的汉字，和计算机转换的规则，

#
# filename = "lambda表达式.py"  # 获取文件名，，，读取含有英文
#
# # encoding="utf-8"显示文件内容编码格式，同时内容全部转为utf-8格式
# f = open(filename, "r", encoding="utf-8")
# text = f.read()
# print(text)
# f.close()
# print(text)

f = open("text3.txt", "w", encoding="utf-8")
f.write("kjahkdj")

f.close()
# f = open("test1.txt", "r", encoding="utf-8")
# f.write("第二次测试")
# file = f.read()
# print(file)
# f.close()
# print(file)
# str = f.read(3)
# print(str)

# /r:换行；/n:换段落

# f = open("test2.txt", "r", encoding="utf-8")
# # f.write("kkfjahdshfa;shf;jashdfl;khasl;dfh")
# str = f.read()
# print(str)
# # 返回指针当前文件的读写位置，值是当前位置距离文件开头的直接数
# print(f.tell())
#
# print(str)
# f.close() /r/n



# 读数据
# f = open("test.txt", "r")
#
#
# #  read(): 会读取文件内容，并返回内容字符串
# s = f.read()
# print(s)

# import os
#
# filepath = '..\..\Administrator\Desktop'
# files = os.listdir('..\..\Administrator\Desktop')
# filename = '404Error.txt'
# fullname = (os.sep).join([filepath, filename])
# with open(fullname) as f:
#     s = f.read()
# print(s)
# """Unicode"""


