# dictionary:有键值对组成
info = {"name": "python", "age": 26, "id": 110, 0: "number"}
print(info["name"])
print(info[0])  # 字典不能通过下标取值，只能通过健名来取值


# 集合 : 可去重

set1 = {1, 2, 3, 2, 2, 1, 9, 4}
list1 = {1, 2, 3, 2, 2, 1, 9, 4}

print(set1)
print(set(list1))

# 1、创建字典
# fromkeys()
num_dict = {}
l = num_dict.fromkeys(["aa", "b"], 10) # 第一个参数是序列，第二个参数是固定值
print(l)
# 2、根据键名添加修改
# 如果字典没有这个键，则创建这个键值对,如果有这个键值对，则重新赋值

name_dict = {}
name_dict["name"] = "python"
print(name_dict)
name_dict["name"] = "JAVA"
print(name_dict)
# 3、setdefault():

print(name_dict.setdefault("name"))
# 如果有这个键，则返回这个键的值，如果没有这个键，就返回None，同时创建键值对，值为None
print(name_dict.setdefault("id", 100))
name_dict.setdefault("le", 20)
print(name_dict)


# 3、keys():返回这个字典的所有的键的列表

keys_dict = {"id": 1001, "bookNmae": "从你的全世界路过", "autor": "Alio"}
L = keys_dict.keys()
print(L)

# 4、values(): 返回这个字典的所有的值的列表
print(keys_dict.values())

# 5、返回这个字典所有的键值对（元组）的列表
print(keys_dict.items())
for Lo in keys_dict.items():
    print(list(Lo))


