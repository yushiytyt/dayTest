mystr = "hello nvsheng hello python"
# 1、用字符串的方法
# ch_list = []
# for new_str in mystr:
#     if new_str not in ch_list:
#         print("字符串%s的个数为：%d个" % (new_str, mystr.count(new_str)))
#         ch_list.append(new_str)

# ord(ch):字符转成ascii码
# chr(ascii)-->chr


#2、 用列表处理
count_list = [0] * 127
for new_list in mystr:
    count_list[ord(new_list)] += 1  # 将指定下标元素自增1，
for index, num in enumerate(count_list):  # 值就是字符的个数
    if num != 0:
        print("字符%s的个数为%d：" % (chr(index), num))


#  3、用字典处理




