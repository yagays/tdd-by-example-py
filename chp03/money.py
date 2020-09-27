class Dollar:
    def __init__(self, amount):
        self.amount: int = amount

    def __eq__(self, o):
        return self.amount == o.amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)
