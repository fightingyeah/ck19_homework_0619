# -*- coding: utf-8 -*-
# @Time : 2021/6/19 11:15
# @Author : Vicky
# @File : calculator_j.py
# @Software: PyCharm

#被测方法 计算器
class Calculator:

    def add(self, a, b):
        try:
            result = a + b
        except Exception as e:
            return "Error"
        else:
            if isinstance(a, float):
                result = round(result, 2)
        return result

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            result = a / b
        except Exception as e:
            return "Error"
        else:
            return result

# result = Calculator().add('str',9)
# print(result)
# error_info = Calculator().div(-5, 'str')
# print(error_info)