from main import func


def test_func():
    value1 = 1
    value2 = 2
    expected = 4
    assert func(value1, value2) == expected
