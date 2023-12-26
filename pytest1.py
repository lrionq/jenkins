import pytest


def setup_function(self):
    print("\n开始计算")


def teardown_function(self):
    print("计算结束")


# 加法
def add_function(a, b):
    return a + b


@pytest.mark.parametrize("a,b,expected", [(1, 2, 3), (-10, -20, -30), (-10, 10, 0), (3.5, 5.5, 9)],
                         ids=["int+int", "minus", "int+minus", "n_int+n_int"])
def test_add(a, b, expected):
    print("\na+b的结果为：" + str(add_function(a, b)), "与预期值比较结果为：", add_function(a, b) == expected)
    assert add_function(a, b) == expected


# 减法
def reduce_function(a, b):
    return a - b


@pytest.mark.parametrize("a,b,expected", [(3, 2, 1), (-10, -20, 10), (-10, 10, -20), (9, 3.5, 5.5)],
                         ids=["int-int", "minus-minus", "minus-int", "n_int-n_int"])
def test_reduce(a, b, expected):
    print("\na-b的结果为：" + str(reduce_function(a, b)), "与预期值比较结果为：", reduce_function(a, b) == expected)
    assert reduce_function(a, b) == expected


# 乘法
def multiplication_function(a, b):
    return a * b


@pytest.mark.parametrize("a,b,expected", [(3, 2, 6), (-10, -20, 200), (-10, 10, -100), (2.5, 4, 10), (2.5, 0.4, 1)],
                         ids=["int*int", "minus*minus", "minus*int", "n_int*int", "n_int*n_int"])
def test_multiplication(a, b, expected):
    print("\na*b的结果为：" + str(multiplication_function(a, b)), "与预期值比较结果为：",
          multiplication_function(a, b) == expected)
    assert multiplication_function(a, b) == expected


# 除法
def division_function(a, b):
    return a / b


@pytest.mark.parametrize("a,b,expected", [(3, 3, 1), (-10, -20, 0.5), (-10, 10, -1), (2.5, 5, 0.5), (2.5, 0.5, 5)],
                         ids=["int/int", "minus/minus", "minus/int", "n_int/int", "n_int/n_int"])
def test_multiplication(a, b, expected):
    print("\na/b的结果为：" + str(division_function(a, b)), "与预期值比较结果为：", division_function(a, b) == expected)
    assert division_function(a, b) == expected
