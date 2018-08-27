# coding=utf-8
import pygame

# 加载并初始化pygame的所有模块

pygame.init()
# hero_rect = pygame.Rect(10, 20, 30, 40)
# print("%d %d" % (hero_rect.x, hero_rect.y))
# print("%d %d" % (hero_rect.width, hero_rect.height))
# print("%d %d" % hero_rect.size)
# print("coding")
# 1、创建主窗口
screen = pygame.display.set_mode((480, 700))

# 2、绘制背景图像
# （1）、加载背景图像
bg = pygame.image.load("./images/background.png")
# (2)绘制背景图像
screen.blit(bg, (0, 0))
# (3)update更新屏幕显示
# pygame.display.update()

# 3、绘制英雄
hero_bg = pygame.image.load("./images/me1.png")
screen.blit(hero_bg, (150, 500))
pygame.display.update()
# 时钟对象
clock = pygame.time.Clock()
# 1、记录飞机的初始位置

hero_rect = pygame.Rect(150, 500, 102, 126)

i = 0
# hero_rect = 500
# 游戏循环
while True:
    clock.tick(60)
    # 捕获事件
    # event_list = pygame.event.get()
    # if len(event_list) > 0:
    #     print(event_list)
    #     print("\n")

    # 事件监听
    for event in pygame.event.get():
        # 事件退出
        if event.type == pygame.QUIT:
            print("游戏退出")
            pygame.quit()
            exit()  #



    # print(i)
    # i += 1
    # 修改飞机位置
    # hero_rect.y -= 1
    # if hero_rect.y <= -126:
    #     hero_rect.y = 700
    # screen.blit(bg, (0, 0))
    # screen.blit(hero_bg, hero_rect)

    # 更新显示
    # pygame.display.update()

    # 绘制图像
    # screen.blit(bg, (0, 0))
    # screen.blit(hero_bg, hero_rect)

    # 更新显示
    # pygame.display.update()
    # pass
    hero_rect.y -= 1
    if hero_rect.y <= -126:
        hero_rect.y = 700
    screen.blit(bg, (0, 0))
    screen.blit(hero_bg, hero_rect)
    pygame.display.update()
# 卸载所有pygame模块，在游戏结束之前调用
pygame.quit()

