import random


class House:
    address: str
    area: int
    cost: int

    def __init__(self, address, area, cost):
        self.address = address
        self.area = area
        self.cost = cost

    def increase_cost(self):
        self.cost = self.cost + random.randint(100, 500)

    def decrease_cost(self):
        self.cost = self.cost - random.randint(100, 500)
