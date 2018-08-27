
mystr = "hello nvsheng hello python"

# 1、用字典统计字符串个数
num_dict = {}
for s in mystr:
    if s not in num_dict:
        num_dict.setdefault(s, 1)
    else:
        num_dict[s] += 1
print(num_dict)

# 2、用列表统计
num_list = []
for s in mystr:
    if s not in num_list:
        print("%s的个数为：%d个" % (s, mystr.count(s)))
        num_list.append(s)


