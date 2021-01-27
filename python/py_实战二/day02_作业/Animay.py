#!/usr/bin/python
# coding=utf-8

# 创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
class Animal:
    def __init__(self,name,colour,age,sex):
        self.name=name
        self.colour=colour
        self.age=age
        self.sex=sex

    def sing(self):
        print("动物都会叫")

    def run(self):
        print("动物都会跑")

