# coding=utf-8
import pygame
from plane_spritess import *


class PlaneGame(object):
    """主游戏类"""
    def __init__(self):
        print("游戏开始")
    #     1、创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
    #     2、创建游戏时钟
        self.clock = pygame.time.Clock()
    #     3、创建精灵和精灵组
        self.__create_sprites()
    #     4、设计定时器时间
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    # 创建精灵
    def __create_sprites(self):
        # print("创建精灵")
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        self.enemy_group = pygame.sprite.Group()

        # self.hero_group = pygame.sprite.Group()

    def start_game(self):
        print("游戏开始……")
        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            # 更新绘制精灵组
            self.__update_sprites()
            pygame.display.update()

    # 事件监听
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出场")
                # 1、创建敌机
                enemy = Enemy()
                # 2、将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)

                # hero = HeroPlane()
                # self.hero_group.add(hero)

    def __check_collide(self):
        pass

    # 更新精灵
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)



    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()

