#!/usr/bin/python

from python.py_实战二.day02_作业.Animay import Animal

"""
创建子类【猫】，继承【动物类】，
- 复写父类的__init__方法，继承父类的属性，
- 添加一个新的属性，毛发=短毛，
- 添加一个新的方法， 会捉老鼠，
- 复写父类的‘【会叫】的方法，改成【喵喵叫】
"""

class cat(Animal):
    def __init__(self,name,colour,age,sex,Shorthair):
        self.name=name
        self.colour=colour
        self.age=age
        self.sex=sex
        # 添加一个新的属性，毛发 = 短毛，
        self.Shorthair=Shorthair

    # 添加一个抓老鼠的方法
    def catching_mice(self):
        return
        print("猫都会抓老鼠")


    def sing(self):
        print("猫会喵喵叫")



