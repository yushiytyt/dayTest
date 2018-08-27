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
    # 构造函数
    def __init__(self, name, skill, hp, atk, armor):
        # 名字
        self.name = name
        # 技能
        self.skill = skill
        # 生命值
        self.hp = hp
        # 攻击
        self.atk = atk
        # 护甲
        self.armor = armor

    """定义一个英雄类，可以移动和攻击"""
    def move(self):
        print("正在前往事发地点")

    def attack(self):
        print("发起了一招强有力的攻击")

    def info(self):
        print("英雄%s的生命值为：%d" % (self.name, self.hp))
        print("英雄%s的攻击力为：%d" % (self.name, self.atk))
        print("英雄%s的技能为：%s" % (self.name, self.skill))


"""如果有多个对象，每个对象的实例变量是各自保存的，有自己独立的内存地址
但是，实例方法是共享的，类通过self来判断是哪个对象调用了实例方法
"""

# 实例化对象之后，会调用init方法
man_wang = Hero("泰达米尔", "旋风斩", 2000, 500, 200)
gai_lun = Hero("盖伦", "正义之剑", 4000, 300, 150)

man_wang.move()
man_wang.attack()
man_wang.info()
gai_lun.move()
gai_lun.attack()
gai_lun.info()

print(man_wang)
print(gai_lun)




