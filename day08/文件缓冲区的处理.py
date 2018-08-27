# coding=gbk
import time

f = open("test6.txt", "w", encoding="utf-8")
f.write("hello word\nhello world2\nhello word3")

# 当程序执行到这里，会暂停5秒，5秒后继续执行
# time.sleep(5)

# 将缓冲区的数据写入到磁盘文件里，并不清空缓冲区，而且也不用关闭文件
f.flush()

# print(f.read())

# 表示将缓冲去的数据写入到磁盘文件中，并清空缓冲区

# f.close()
# 查看文件编码
print(f.encoding)
# 查看文件名
print(f.name)
# 查看文件是否关闭
print(f.close)

