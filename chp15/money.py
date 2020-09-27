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

    def reduce(self, bank, to):
        rate = bank.rate(self._currency, to)
        return Money(self.amount / rate, to)

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")


class Bank:
    def __init__(self):
        self.rates = {}

    def reduce(self, source, to):
        return source.reduce(self, to)

    def add_rate(self, source, to, rate):
        self.rates[(source, to)] = rate

    def rate(self, source, to):
        if source == to:
            return 1
        return self.rates[(source, to)]


class Sum:
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def plus(self, addend):
        return None

    def reduce(self, bank, to):
        amount = self.augend.reduce(bank, to).amount + self.addend.reduce(bank, to).amount
        return Money(amount, to)
