from sample_1 import plus


def test_plus():
    value1 = 1
    value2 = 2
    expected = 3
    assert plus(value1, value2) == expected
