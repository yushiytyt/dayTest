"""
基本功能
1、添加名片
2、删除名片
3、修改名片
4、查询名片
5、退出系统
要求：程序运行后，除非选择退出系统，否则重复执行功能
"""
# 复习
# mystr = "hello nvsheng hello python"
# 要求：统计字符串中各字符的个数
# 方法一：
# num_list = []
# for new_list in mystr:
#     if new_list not in num_list:
#         print(new_list, mystr.count(new_list))
#         # new_list
#         num_list.append(new_list)
# 方法二：利用ASSIC来

# my_list = [0] * 127
# for new_list in mystr:
#     my_list[ord(new_list)] += 1
#
# for index, num in enumerate(my_list):
#     if num != 0:
#         print(chr(index), num)

#
# 1、创建一个列表，用来存储名片信息
name = "admin"
password = "123456"
info_list = []
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

                # 添加
                if myNum == 1:
                    name = input("请输入姓名")
                    age = input("请输入年龄")
                    sex = input("请输入性别")
                    info_list.append([name, age, sex])
                    # print(info_list)
                    print("[INFO]:存储成功！")
                    print(info_list)

                # 删除[[], [], []]
                elif myNum == 2:
                    print(info_list)
                    delName = input("请输入要删除的姓名：")
                    for info in info_list:
                        if delName in info:
                            info_list.remove(info)
                            print(info_list)
                            print("[INFO]:删除成功")
                            break  # 找到了就不要继续找了
                        else:
                            print("查无此人")
                # 修改
                elif myNum == 3:
                    updateName = input("请输入要修改的姓名")
                    for info in info_list:
                        if updateName in info:
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

                # 查询
                elif myNum == 4:
                    selName = input("请输入要查询的姓名：")
                    for info in info_list:
                        if selName in info:
                            print(info)
                            print("[INFO]:查询成功")
                            break
                        else:
                            print("[EROOR]:查无此人")
                # 退出
                elif myNum == 5:
                    print("系统退出")
                    break
    else:
        print("账号或密码错误，请重新输入")














