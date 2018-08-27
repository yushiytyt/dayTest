# """
#     文件缓冲区的处理
# """
# import time
#
# f = open("test6.txt", "w", encoding="utf-8")
# f.write("hello word\nhello world2\nhello word3")
# # 将缓冲区的数据写入到磁盘文件里，并不清空缓冲区，而且也不用关闭文件
#
#
# # 表示将缓冲去的数据写入到磁盘文件中，并清空缓冲区
#
#
# f.close()

f = open("test6.txt", "w", encoding="utf-8")
f.write("hello world1\nhello world2\nhello world3\nhello world4")
f.close()
f = open("test5.txt", "r", encoding="utf-8")
neiRong = f.read()
print(neiRong)


