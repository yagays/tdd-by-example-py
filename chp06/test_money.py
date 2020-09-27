import pytest

from money import Dollar, Franc


def test_multiplication():
    five = Dollar(5)
    assert Dollar(10) == five.times(2)
    assert Dollar(15) == five.times(3)


def test_equality():
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)
    assert Franc(5) == Franc(5)
    assert Franc(5) != Franc(6)


def test_franc_multiplication():
    five = Franc(5)
    assert Franc(10) == five.times(2)
    assert Franc(15) == five.times(3)
