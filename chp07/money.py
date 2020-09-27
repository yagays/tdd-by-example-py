class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, o):
        return self.amount == o.amount and self.__class__ == o.__class__


class Dollar(Money):
    def __init__(self, amount):
        self.amount: int = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


class Franc(Money):
    def __init__(self, amount):
        self.amount: int = amount

    def times(self, multiplier):
        return Franc(self.amount * multiplier)
