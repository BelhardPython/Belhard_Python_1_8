from tasks.medium.realt.house import House
from tasks.medium.realt.person import Person
from tasks.medium.realt.townhouse import Townhouse

if __name__ == '__main__':
    house_one = House('St. Sosnovaya - 12', 50, 1500)
    house_two = House('St. Everdine - 1', 40, 2000)
    townhouse_one = Townhouse('St. Lancester - 10', 60, 2500)
    townhouse_two = Townhouse('St. Hungers - 12', 25, 1100)
    person_1 = Person('John', 35)
    person_1.earn_money()
    person_1.make_deal(house_one)
    person_1.earn_money()
    person_1.earn_money()
    person_1.earn_money()
    person_1.make_deal(townhouse_two)
    person_1.earn_money()
    person_1.make_deal(townhouse_two)
    person_1.make_deal(townhouse_one)
    person_1.make_deal(house_one)
    person_1.earn_money()
    person_1.earn_money()
    person_1.earn_money()
    person_1.make_deal(house_two)
    person_1.make_deal(house_one)
    person_1.make_deal(townhouse_one)
    person_1.make_deal(house_two)
