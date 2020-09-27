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

    @staticmethod
    def dollar(amount):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount):
        return Franc(amount, "CHF")


class Dollar(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)


class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
