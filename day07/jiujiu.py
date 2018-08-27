# line = 10
# for i in line:
#     print("*")
# line = 1
# while line <= 9:
#     num = 1
#     while num <= line:
#         print("*")
#         num += 1
#     line += 1
# line = 1
# while line <= 9:
#     num = 1
#     while num <= line:
#         print("*")
#         num += 1


def func1():
    for i in range(1, 10):
        for j in range(1, i+1):
            print("%d * %d = %2d" % (j, i, j*i), end="  ")
        print()


func1()
