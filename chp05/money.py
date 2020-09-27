class Dollar:
    def __init__(self, amount):
        self.__amount: int = amount

    def __eq__(self, o):
        return self.__amount == o.__amount

    def times(self, multiplier):
        return Dollar(self.__amount * multiplier)


class Franc:
    def __init__(self, amount):
        self.__amount: int = amount

    def __eq__(self, o):
        return self.__amount == o.__amount

    def times(self, multiplier):
        return Franc(self.__amount * multiplier)
