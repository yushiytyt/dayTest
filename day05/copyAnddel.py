# copy(): 深拷贝字典，创建一个新的字典对象。

name_dict = {"name": "python", "age": 26, "id": 110}

# pop():参数是键，删除指定的键值对,并返回值（第二个参数表示如果没有这个键值队，则返回这个值）
print(name_dict)
newName_dict = name_dict.copy()
print(newName_dict)

newName_dict.pop("name")
print(newName_dict)
INFO = newName_dict.pop("newName", "没有这个键")  # 有这个键就删除这个键，没有就返回第二个参数的值
print(INFO)

# popitem(): 依次，从后向前 删除键值对，并返回这个键值对的 元组

name_dict1 = {"name": "python", "age": 26, "id": 110}
key, value = name_dict1.popitem()  # 拆包(拆分元组， 并用变量接收)
print(key, value)

# 删除
# name_dict1.clear()
# print(name_dict1)

del name_dict1
print(name_dict1)