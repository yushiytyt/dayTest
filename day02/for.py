age = int(input("请输入你的年龄："))

if age >= 18:
    print("欢迎光临本网吧、请出示身份证准备上网")
else:
    print("本网版禁止未成年人上网")

score = int(input("请输入考试成绩"))
if 80 <= score < 100:
    print("A")
elif 60 <= score < 80:
    print("B")
else:
    print("C")

cheP = 1
daoLength = 9

if cheP == 1:
    print("进站")
    if daoLength <= 9:
        print("安全")
        print("一起度蜜月")
    else:
        print("进派出所")
else:
    print("没有车票、不能上车")
    print("拜拜、下次见！")

see = 1

if see == 1:
    print("maiyigebaozi")
else:
    print("buxiaode")


xiaBan = 1
xiGua = 0
baoZi = 1
if xiaBan:
    baoZi = 10
    if xiGua:
        baoZi = 1
# 标准
cp = 1
dj = 10
yt = 80

if cp:
    if dj <= 10:
        if yt <= 80:
            print("安全")
        else:
            print("不安全")
    else:
        print("不安全")
else:
    print("无法通过")
if cp and dj <= 10 and yt <= 80:
    print("tonguo")
else:
    print("不安全")


"""
    比较运算符（>、<、>=、<=、！=、<>）、逻辑运算符（and、or、not）、
"""
