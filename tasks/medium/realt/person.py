import random


class Person:
    name: str
    age: int
    money: int
    realty: list

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.money = 0
        self.realty = []

    def info(self):
        return self.name, self.age, self.realty, self.money

    def earn_money(self):
        self.money += random.randint(1500, 2000)

    def make_deal(self, house):
        if self.money >= house.cost:
            self.money -= house.cost
            self.realty.append(house)
        else:
            print('Not enough money')
