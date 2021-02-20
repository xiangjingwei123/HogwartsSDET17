#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import allure
import pytest
import yaml

sys.path.append('..')
print(sys.path)
from pythoncode.Calculator import Calculator


def get_datas(name, type='int'):
    with open("./datas/calc.yml", encoding='utf-8') as f:
        all_datas = yaml.safe_load(f)
    datas = all_datas[name][type]['datas']
    ids = all_datas[name][type]['ids']
    return (datas, ids)


@pytest.fixture()
def get_instance():
    print("开始计算")
    calc: Calculator = Calculator()
    yield calc
    print("结束计算")


@pytest.fixture(params=get_datas('add', 'int')[0], ids=get_datas('add', 'int')[1])
def get_datas_with_fixture(request):
    return request.param


def test_param(get_datas_with_fixture):
    print(get_datas_with_fixture)


# yaml json excel csv xml
# 测试类
@allure.feature("计算器")
class TestCalc:
    # datas: list = get_datas()
    add_int_data = get_datas('add', 'int')
    div_int_data = get_datas('div', 'int_error')

    # @pytest.mark.parametrize("a, b, result", add_int_data[0], ids=add_int_data[1])
    # def test_add(self,get_instance, a, b, result):
    #     assert result == get_instance.add(a, b)

    @allure.title("相加_{get_datas_with_fixture[0]}_{get_datas_with_fixture[1]}")
    @allure.story("相加功能")
    def test_add(self, get_instance, get_datas_with_fixture):
        f = get_datas_with_fixture
        assert f[2] == get_instance.add(f[0], f[1])

    # @pytest.mark.parametrize("a,b,result", [
    #     [-1, -2, -3],
    #     [0.1, 0.2, 0.3]
    # ])
    # def test_add_float(self, get_instance, a, b, result):
    #     print(f"a={a},b={b},result={result}")
    #     assert result == round(get_instance.add(a, b), 2)

    # TODO: 完善相加功能
    @pytest.mark.parametrize("a, b, result", add_int_data[0], ids=add_int_data[1])
    def test_add1(self,get_instance, a, b, result):
        print(f"a={a}, b={b}, result={result}")
        assert result== get_instance.add(a,b)


    # TODO: 相除功能
    @pytest.mark.parametrize("a, b, result", div_int_data[0], ids=div_int_data[1])
    def test_div(self, get_instance, a, b, result):
        if result== round(get_instance.div(a, b)):
            assert result== round(get_instance.div(a, b))
        elif b==0:
            with pytest.raises(ZeroDivisionError):
                print('除数不可以为0') #12



