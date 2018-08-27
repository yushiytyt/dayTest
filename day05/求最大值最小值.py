# """
# 编程实现对一个元素全为数字的列表，求最大最小值
# """
# 方法一：先排序
num_list = [10, 20, 20, 100, 5, 129, -100]
num_list.sort()
min1 = num_list[0]
print("列表中最小值为：%d" % min1)
max1 = num_list[len(num_list) - 1]
print("列表中最大值为：%d" % max1)

# 方法二：循环比较
num_list2 = [10, 20, 20, 100, 5, 129, -100]
max_num = 0
for num in num_list2:
    if max_num < num:
        max_num = num
    if max_num > num:
        min_num = num
print(max_num)
print(min_num)
