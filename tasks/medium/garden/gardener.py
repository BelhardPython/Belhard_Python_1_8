class Gardener:
    name: str
    plants: list

    def __init__(self, name, *args):
        self.name = name
        self.plants = []
        for arg in args:
            self.plants.append(arg)

    def work(self):
        for tomato_bush in self.plants:
            tomato_bush.grow_all()

    def harvest(self):
        if all([tomato_bush.all_are_ripe for tomato_bush in self.plants]):
            result = []
            for i in self.plants:
                result += i.give_away_all()
            return result
        else:
            print("Томаты еще не созрели")
            return None
