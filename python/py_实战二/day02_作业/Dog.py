#!/usr/bin/python

from python.py_实战二.day02_作业.Animay import Animal
"""
创建子类【狗】，继承【动物类】，
- 复写父类的__init__方法，继承父类的属性，
- 添加一个新的属性，毛发=长毛，
- 添加一个新的方法， 会看家，
- 复写父类的【会叫】的方法，改成【汪汪叫】
"""

class dog(Animal):
    def __init__(self,name,colour,age,sex,longhair):
        self.name=name
        self.colour=colour
        self.age=age
        self.sex=sex
        self.longhair=longhair

    # 会看家的方法
    def Caretaker(self):
        return
        print("狗会看家")

    #狗会叫的方法
    def sing(self):
        print("狗会汪汪叫")



        
