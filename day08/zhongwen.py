# """
#     �ļ��������Ĵ���
# """
# import time
#
# f = open("test6.txt", "w", encoding="utf-8")
# f.write("hello word\nhello world2\nhello word3")
# # ��������������д�뵽�����ļ��������ջ�����������Ҳ���ùر��ļ�
#
#
# # ��ʾ������ȥ������д�뵽�����ļ��У�����ջ�����
#
#
# f.close()

f = open("test6.txt", "w", encoding="utf-8")
f.write("hello world1\nhello world2\nhello world3\nhello world4")
f.close()
f = open("test5.txt", "r", encoding="utf-8")
neiRong = f.read()
print(neiRong)


