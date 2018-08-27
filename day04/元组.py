"""
元组与列表相似，不同之处在于元组的元素不能修改，元组使用小括号，列表使用方括号
没有元组推导式
有列表推导式，字典推导式，

"""
tuple1 = (10, 20, 30)
print(tuple1)
tl = tuple(range(10, 20, 2))
print(tl)
t4 = (i for i in range(10, 30, 1) if i % 2 == 0)
for i in t4:
    print(i)

