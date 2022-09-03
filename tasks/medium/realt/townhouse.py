from tasks.medium.realt.house import House


class Townhouse(House):
    def __init__(self, address, area, cost):
        super().__init__(address, area, cost)
        self.area = 60
