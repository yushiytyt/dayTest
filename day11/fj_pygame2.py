# coding=utf-8
# import sys
import pygame
from plane_sprites import *

pygame.init()
# 1、创建游戏主窗口、第一个参数元组表示窗口的尺寸
screen = pygame.display.set_mode((480, 700))

# 2、将图片加载到内存
bg = pygame.image.load("./images/background.png")

# 3、将图片绘制到主窗口
screen.blit(bg, (0, 0))
# 4、显示图像
pygame.display.update()

# 5、创建英雄对象
hero_bg = pygame.image.load("./images/me1.png")
screen.blit(hero_bg, (165, 574))
pygame.display.update()

# 6、制作英雄移动动画
# (1)创建始终对象
clock = pygame.time.Clock()
# （2）记录初始位置
hero_rect = pygame.Rect(165, 574, 102, 126)

#  创建游戏精灵、游戏精灵组

enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)
enemy_group = pygame.sprite.Group(enemy, enemy1)


# 游戏循环

while True:
    clock.tick(60)

    # 创建事件监听
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            print("游戏退出……")
            pygame.quit()
            exit()

    hero_rect.y -= 1
    if hero_rect.y <= -126:
        hero_rect.y = 700
    screen.blit(bg, (0, 0))
    screen.blit(hero_bg, hero_rect)
    # 精灵组调用方法
    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.update()
    pass

pygame.quit()
