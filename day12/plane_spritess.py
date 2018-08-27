# coding=utf-8
import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)  # 图像数据源
        self.rect = self.image.get_rect()
        self.speed = speed  # 移动速度

    #
    def update(self):
        self.rect.y += self.speed
    # def update(self):


class Background(GameSprite):
    """游戏背景精灵"""
    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")

        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        super().__init__("./images/enemy1.png")

        self.speed = random.randint(1, 3)

    #     指定敌机的初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:

            self.kill()
            pass
            # print("敌机飞出屏幕")
            # 销毁飞出的对象，释放内存

    # 对象销毁钱会被调用
    def __del__(self):
        print("敌机被销毁%s" % self.rect)


# 英雄类 1、游戏启动后，英雄会出现在屏幕的水平中间位置，距离屏幕底部120像素
# 2、每隔0.5秒发射一次子弹，每次连发三枚子弹
# 3、英雄默认不会移动，需要通过左右方向键。控制英雄在水平方向移动
# class HeroPlane(GameSprite):
#     def __init__(self):
#         # 1、调用父类方法
#         super().__init__("./images/me1.png")
#         # 指定英雄初始位置
#         self.rect.x = (SCREEN_RECT - self.rect.width) / 2
#         self.rect.bottom = 20
#         pass
#
#     def update(self):
#         super().update()
#         self.speed = 0
#         pass
