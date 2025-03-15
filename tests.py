from functions import sum_all_and_multiply_by_2


def test_1():
    assert sum_all_and_multiply_by_2(1, 2, 3) == 12

def test_2():
    assert sum_all_and_multiply_by_2(0, 2, 3) == 10

def test_3():
    assert sum_all_and_multiply_by_2(1, 2, 3, 4, 5, 6) == 42