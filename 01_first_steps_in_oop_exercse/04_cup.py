class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self. quantity = quantity

    def fill(self, quantity):
        if self.size >= quantity + self.quantity:
            self.quantity += quantity
            return self.quantity

    def status(self):
        result = self.size - self.quantity
        return result


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
