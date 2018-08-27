"""
PEP8标准：类或者函数前后都要空两行
"""


def my_function():
    """
    函数的文档说明：
    :return:
    """
    print("this is my first Python Function")


my_function()

"""
基本功能
1、添加名片
2、删除名片
3、修改名片
4、查询名片
5、退出系统
要求：程序运行后，除非选择退出系统，否则重复执行功能
"""
# 1、创建一个列表，用来存储名片信息
name = "admin"
password = "123456"
info_list = []

# 登入


def add_ming_pia():
    name = input("请输入姓名")
    age = input("请输入年龄")
    sex = input("请输入性别")
    info_list.append([name, age, sex])
    print("[INFO]:存储成功！")
    print(info_list)


def del_ming_pia():
    print(info_list)
    del_name = input("请输入要删除的姓名：")
    for info in info_list:
        if del_name in info:
            info_list.remove(info)
            print(info_list)
            print("[INFO]:删除成功")
            break  # 找到了就不要继续找了
        else:
            print("查无此人")


def update_ming_pia():
    update_name = input("请输入要修改的姓名")
    for info in info_list:
        if update_name in info:
            newName = input("新姓名：")
            newAge = input("新年龄：")
            newSex = input("新性别：")
            # 找到位置进行修改
            info_list[info_list.index(info)] = [newName, newAge, newSex]
            print("[INFO]:修改成功")
            print(info_list)
            break
        else:
            print("查无此人")


def select_ming_pia():
    selName = input("请输入要查询的姓名：")
    for info in info_list:
        if selName in info:
            print(info)
            print("[INFO]:查询成功")
            break
        else:
            print("[EROOR]:查无此人")


while True:
    sName = input("账号：")
    sPassWord = input("密码：")
    if sName == name and sPassWord == password:
        print("登入成功==欢饮使用名片管理系统")
        while True:
            print("=" * 120)
            print("1：添加名片  2：删除名片  3：修改名片  4：查询名片  5：退出系统")
            print("=" * 120)
            myNum = int(input("请输入要选择的操作序号："))
            num_list = [1, 2, 3, 4]
            if myNum not in num_list:
                print("[EROOR]:请输入正确的数字")
            else:
                if myNum == 1:
                    add_ming_pia()

                elif myNum == 2:
                    del_ming_pia()

                elif myNum == 3:
                    update_ming_pia()

                elif myNum == 4:
                    select_ming_pia()

                elif myNum == 5:
                    print("系统退出")
                    break
    else:
        print("账号或密码错误，请重新输入")