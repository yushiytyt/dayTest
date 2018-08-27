# import copy
# dic1 = {"naem": "python"}
# print(id(dic1))
# dic2 = dic1.copy()
# print(id(dic2))
# dic3 = copy.deepcopy(dic1)
# # dic4 = copy.deepcopy(dic2)
# print(id(dic3))
# dic4 = copy.deepcopy(dic2)
# print(id(dic4))

# 1、将2个列表元素合并为一个字典
# key_list = ["name", "age", "id"]
# value_list = ["python", 18, 110]
# new_dic = {key_list[i]: value_list[i] for i in range(len(key_list))}
# print(new_dic)

# 2、字典推导式
# num_dict = {i: i ** 2 for i in range(1, 10)}
# print(num_dict)

name_dict = {"name": "python", "age": 26, "id": 110}
key_list = []
value_list = []

#  3、字典转成2个列表
for key, value in name_dict.items():
    key_list.append(key)
    value_list.append(value)
print(key_list)
print(value_list)
# print(name_dict.items())

# 4、字典的键值对相互转换

