#!/usr/bin/python

from python.py_实战二.day02_作业.Cat import cat
from python.py_实战二.day02_作业.Dog import dog
# 导入包
import yaml
if __name__ == '__main__':
    with open("AN.yml", encoding='UTF-8') as f:
        f1 = yaml.safe_load(f)
        # 调用yaml文件中数据的类
        data1=f1['Animay']
        data2=f1['cat']
        data3=f1['dog']

# 调用yaml文件中cat类的属性
        c1=data2['name']
        c2=data2['colour']
        c3=data2['age']
        c4=data2['sex']
        c5=data2['Shorthair']

# 调用yaml文件中dog类的属性
        d1=data3['name']
        d2=data3['colour']
        d3=data3['age']
        d4=data3['sex']
        d5=data3['longhair']

"""
创建一个猫猫实例
调用捉老鼠的方法
打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
"""
catcat=cat(c1,c2,c3,c4,c5)
catcat.catching_mice()
print(f"猫猫的属性:{c1,c2,c3,c4,c5}")

"""
创建一个狗狗实例
- 调用【会看家】的方法
- 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
"""
dogdog = dog(d1,d2,d3,d4,d5)
dogdog.Caretaker()
print(f"狗狗的属性:{d1,d2,d3,d4,d5}")