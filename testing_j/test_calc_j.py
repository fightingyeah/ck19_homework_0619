# -*- coding: utf-8 -*-
# @Time : 2021/6/19 10:50
# @Author : Vicky
# @File : test_calc_j.py
# @Software: PyCharm

def add(a, b):
    return a+b

def test_add1():
    print("1+1==2")
    assert 2 == add(1, 1)

def test_add2():
    print("1+3==4")
    assert 4 == add(1, 3)