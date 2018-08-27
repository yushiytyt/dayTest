num_list = [123, 124, 0, -8, 100]
print(num_list)
# num_list.sort()：默认False，从小到大
num_list.sort(reverse=True)
print(num_list)
# sort:在元列表的基础上修改，
# sorted：生成一个新的列表，，同样的，reverse=Ture 表示从小到大排序