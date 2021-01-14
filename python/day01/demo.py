#!/usr/bin/python
# coding=utf-8
'''
创建模块，模块里面创建方法，定义有参数，和无数，
有返回值和无返回值 的情况，并说明 无返回值的默认返回值。
'''


# 定义一个名为fun的方法，并传参
def fun(a, b):
    c = a + b
    # 将求和的值返回给c,然后结果返回到fun方法中
    return c


def fun1():
    # 无参数的返回值为‘None’
    return


if __name__ == '__main__':
    print("有返回值:", fun(50, 50))
    print("无返回值:", fun1())
