# coding=gbk
import os

# 1�����ص�ǰ�ļ��ľ���·��
# file_name = os.getcwd()
# print(file_name)

# 2���ж��ļ��Ƿ����,���ڷ���True���������򷵻�False

# print(os.path.exists(r".\test.txt"))

# 3��ɾ��ָ��·�����ļ�
# os.remove(r".\test.txt")

# 4����ָ���ļ�������,os.rename(old_name, new_name)
# os.rename("test.txt", "test1.txt")

# 5����ȡ��ǰĿ¼�µ������ļ�(Ĭ���ǵ�ǰĿ¼������ָ��Ŀ¼)������һ���б�
# file_name_list = os.listdir(r"C:\Users\Administrator\Desktop")
# f = open("pp.txt", "r", encoding="utf-8")
# print(file_name_list)
# for file_hlc in file_name_list:
#     if "pp.txt" in file_hlc:
#         # print("pp.txt".read())
#         print("aa")
#     else:
#         print("�ļ�������")
# fil = open("pp.txt", "r", encoding="utf-8")
# for hlc_file in file_name_list:
#     if 'pp.txt' in hlc_file:
#         fil.close()
#         print(fil.read())
#     else:
#         print("[ERROR]")


# 6������һ��Ŀ¼�ļ�
# os.mkdir(r"C:\Users\Administrator\Desktop", TEST)
# os.mkdir("")
# file_name = os.getcwd()
# print(file_name)
# os.mkdir(r"G:\pycode2")


# 7����ָ��λ�ô����༶Ŀ¼ r:����������ַ�
# os.makedirs(r"")


# 8��ɾ��ָ��·��һ��Ŀ¼

# os.rmdir(r"G:\pycode1")
# file_name = os.listdir(r"G:\A")
# print(file_name)

# 9��ɾ���༶Ŀ¼
# os.removedirs("")
