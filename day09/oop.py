# coding=utf-8
"""
    oop：面向对象，一种编码规范，编程思想。object oriented programing
    通过类实例化一个对象，通过对象调用类里面的方法
    对象是对类的实例化
    大驼峰、来定义类
    实例方法的第一个参数一定是self，谁调用，表示谁

    __init__(self)

    创建对象后，再去添加属性是不合适的，要创建对象是，就已经有这些属性了

"""


class Hero(object):
    """定义一个英雄类，可以移动和攻击"""
    def move(self):
        print("正在前往事发地点")

    def attack(self):
        print("发起了一招强有力的攻击")


taidamier = Hero()
# 生命值
taidamier.hp = 2000
# 攻击
taidamier.atk = 500
# 护甲
taidamier.armor = 200

print("泰达米尔的生命值为：%d" % taidamier.hp)

taidamier.move()
taidamier.attack()
