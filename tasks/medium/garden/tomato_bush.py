class Tomato:
    index: int
    ripeness: str
    states = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')

    def __init__(self, index):
        self.index = index
        self.ripeness = self.states[0]

    def grow(self):
        if self.ripeness < self.states[3]:
            self.ripeness += 1

    def is_ripe(self):
        if self.ripeness == self.states[3]:
            return True
        else:
            return False
