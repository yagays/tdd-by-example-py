import pytest

from money import Money, Bank, Sum


def test_multiplication():
    five = Money.dollar(5)
    assert Money.dollar(10) == five.times(2)
    assert Money.dollar(15) == five.times(3)


def test_equality():
    assert Money.dollar(5) == Money.dollar(5)
    assert Money.dollar(5) != Money.dollar(6)
    assert Money.franc(5) != Money.dollar(5)


def test_currency():
    assert "USD" == Money.dollar(1).currency()
    assert "CHF" == Money.franc(1).currency()


def test_simple_addition():
    five = Money.dollar(5)
    sum = five.plus(five)
    bank = Bank()
    reduced = bank.reduce(sum, "USD")
    assert Money.dollar(10) == reduced


def test_plus_return_sum():
    five = Money.dollar(5)
    result = five.plus(five)
    assert five == result.augend
    assert five == result.addend


def test_reduce_sum():
    sum = Sum(Money.dollar(3), Money.dollar(4))
    bank = Bank()
    result = bank.reduce(sum, "USD")
    assert Money.dollar(7) == result


def test_reduce_money():
    bank = Bank()
    result = bank.reduce(Money.dollar(1), "USD")
    assert Money.dollar(1) == result


def test_reduce_money_different_currency():
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result = bank.reduce(Money.franc(2), "USD")
    assert Money.dollar(1) == result


def test_identity_rate():
    assert 1 == Bank().rate("USD", "USD")


def test_mixed_addition():
    five_bucks = Money.dollar(5)
    ten_francs = Money.franc(10)
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result = bank.reduce(five_bucks.plus(ten_francs), "USD")
    assert Money.dollar(10) == result


def test_sum_plus_money():
    five_bucks = Money.dollar(5)
    ten_francs = Money.franc(10)
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    sum = Sum(five_bucks, ten_francs).plus(five_bucks)
    result = bank.reduce(sum, "USD")
    assert Money.dollar(15) == result


def test_sum_times():
    five_bucks = Money.dollar(5)
    ten_francs = Money.franc(10)
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    sum = Sum(five_bucks, ten_francs).times(2)
    result = bank.reduce(sum, "USD")
    assert Money.dollar(20) == result