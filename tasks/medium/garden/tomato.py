class TomatoBush:
    tomato_list = list

    def __init__(self, *args):
        self.tomato_list = []
        for arg in args:
            self.tomato_list.append(arg)

    def grow_all(self):
        for tomato in self.tomato_list:
            tomato.grow()

    def all_are_ripe(self):
        if all([tomato.is_ripe() for tomato in self.tomato_list]):
            return True
        else:
            return False

    def give_away_all(self):
        tomatoes = []
        for tomato in self.tomato_list:
            tomatoes.append(tomato.index)
        self.tomato_list.clear()
        return tomatoes
