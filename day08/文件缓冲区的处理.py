# coding=gbk
import time

f = open("test6.txt", "w", encoding="utf-8")
f.write("hello word\nhello world2\nhello word3")

# ������ִ�е��������ͣ5�룬5������ִ��
# time.sleep(5)

# ��������������д�뵽�����ļ��������ջ�����������Ҳ���ùر��ļ�
f.flush()

# print(f.read())

# ��ʾ������ȥ������д�뵽�����ļ��У�����ջ�����

# f.close()
# �鿴�ļ�����
print(f.encoding)
# �鿴�ļ���
print(f.name)
# �鿴�ļ��Ƿ�ر�
print(f.close)

