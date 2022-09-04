from tasks.medium.garden.gardener import Gardener
from tasks.medium.garden.tomato import Tomato
from tasks.medium.garden.tomato_bush import TomatoBush

if __name__ == '__main__':
    tomato_bush_1 = TomatoBush(Tomato(2), Tomato(1), Tomato(4))
    tomato_bush_2 = TomatoBush(Tomato(3), Tomato(5), Tomato(1), Tomato(3))
    gardener = Gardener('Emi', tomato_bush_1, tomato_bush_2)
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.work()
    gardener.harvest()
