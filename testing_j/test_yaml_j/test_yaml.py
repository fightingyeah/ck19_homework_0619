# -*- coding: utf-8 -*-
# @Time : 2021/6/19 15:41
# @Author : Vicky
# @File : test_yaml.py
# @Software: PyCharm
import yaml

def test_demo():
    with open('datas.yml') as f:
        totals = yaml.safe_load(f)
    return (totals)