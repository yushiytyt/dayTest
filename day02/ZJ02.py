import random

sum = "Y"
while sum == "Y":
    # 生成随机数
    computer = random.randint(1, 3)
    # 玩家数据
    player = int(input("请玩家下注1、2、3、4"))
    if player == 4:
        print("游戏退出")
    else:
        if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
            print("玩家胜利")
        elif player == computer:
            print(" 平局")
        else:
            print("玩家失败")
