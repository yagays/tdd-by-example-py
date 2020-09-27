class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self._currency = currency

    def __eq__(self, o):
        return self.amount == o.amount and self._currency == o._currency

    def __repr__(self):
        return f"{self.amount} {self._currency}"

    def currency(self):
        return self._currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self._currency)

    def plus(self, addend):
        return Sum(self, addend)

    def reduce(self, to):
        return self

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")


class Bank:
    def reduce(self, source, to):
        return source.reduce(to)


class Sum:
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, to):
        amount = self.augend.amount + self.addend.amount
        return Money(amount, to)
