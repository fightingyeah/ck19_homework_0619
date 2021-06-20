# -*- coding: utf-8 -*-
# @Time : 2021/6/19 11:17
# @Author : Vicky
# @File : test_calculator_j.py
# @Software: PyCharm
import logging
import pytest
import yaml
from pythoncode.calculator_j import Calculator

def get_calc_data():
    with open('./datas/calc.yml') as f:
        totals = yaml.safe_load(f)
    return (totals['datas_add'],totals['ids_add'],totals['datas_div'],totals['ids_div'])

def test_getdatas():
    logging.info(get_calc_data())

class TestCalculator:

    def setup_class(self):
        logging.info("开始计算")
        #加self后，变成了实例变量，可以在其他用例中调用
        self.calc = Calculator()

    def teardown_class(self):
        logging.info("结束计算")

    @pytest.mark.add
    @pytest.mark.parametrize('a, b, expect', get_calc_data()[0], ids=get_calc_data()[1])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.div
    @pytest.mark.parametrize('a, b, expect', get_calc_data()[2], ids=get_calc_data()[3])
    def test_div(self, a, b, expect):
        assert expect == self.calc.div(a, b)
