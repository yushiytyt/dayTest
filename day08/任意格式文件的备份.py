# coding=utf-8
import os

file_path = os.getcwd()
file_name_list = os.listdir(file_path)
print(file_name_list)
my_file = input("请输入要查询的文件名：")
# for my_file_list in file_name_list:
if my_file not in file_name_list:
    print("[ERROR:]not found the file 'my_file'")
else:
    postion = my_file.rfind(".")
    newfile_name = my_file[:postion] + "_backup" + my_file[postion:]
    print(postion)
    print(newfile_name)

source_file = open(my_file, "rb")
backup_file = open(newfile_name, "wb")

data = source_file.read(10)
# 新建一个文件，把要拷贝的文件写入到这个文件里
backup_file.write(data)
# read()会读取所有的内容，如果文件过大，会导致打开失败，
# data = source_file.read()

print(data)

backup_file.close()
source_file.close()

