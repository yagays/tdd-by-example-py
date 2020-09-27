class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self._currency = currency

    def __eq__(self, o):
        return self.amount == o.amount and self.__class__ == o.__class__

    def currency(self):
        return self._currency

    @staticmethod
    def dollar(amount):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount):
        return Franc(amount, "CHF")


class Dollar(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def times(self, multiplier):
        return Money.dollar(self.amount * multiplier)


class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def times(self, multiplier):
        return Money.franc(self.amount * multiplier)
