# coding=utf-8
card_info_save = []


def add_card_info():
    name_info = input("请输入姓名：")
    age_info = input("请输入年龄：")
    sex_info = input("请输入性别：")
    card_info_save.append([name_info, age_info, sex_info])
    print(card_info_save)
    print("[INFO]:用户信息存储成功")


def del_card_info():
    del_name = input("请输入要删除的用户：")
    for del_info in card_info_save:
        if del_name in del_info:
            # card_info_save[card_info_save.index(del_info)].remove()
            card_info_save.remove(del_info)
            print(del_info)
            print("[INFO]:用户信息删除成功")
            break
        else:
            print("[ERROR]:系统内不存在此用户")


def update_card_info():
    update_name = input("请输入要修改的用户名：")
    for update_info in card_info_save:
        if update_name in update_info:
            new_card_name = input("请输入新用户姓名：")
            new_card_age = input("请输入新用户年龄：")
            new_card_sex = input(" 请输入用户新性别：")
            card_info_save[card_info_save.index(update_info)] = [new_card_name, new_card_age, new_card_sex]
            print("[INFO]:用户信息修改成功")
            break
        else:
            print("[ERROR]:系统内不存在此用户")


def select_card_info():
    select_name = input("请输入要查询的用户姓名：")
    for select_info in card_info_save:
        if select_name in select_info:
            print(card_info_save[card_info_save.index(select_info)])
        else:
            print("[ERROR]:系统内不存在此用户")


# def save_info():


while True:
    user_index = int(input("请选择要操作的功能："))
    if user_index == 1:
        add_card_info()
    elif user_index == 2:
        del_card_info()
    elif user_index == 3:
        update_card_info()
    elif user_index == 4:
        select_card_info()


