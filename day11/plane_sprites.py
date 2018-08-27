# coding=utf-8
import pygame


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵类"""

    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()
        self.image = pygame.image.load(image_name)  # 图片数据
        self.rect = self.image.get_rect()  # 矩形区域
        self.speed = speed  # 运动速度

    # 重写父类update方法

    def update(self, *args):
        self.rect.y += self.speed




