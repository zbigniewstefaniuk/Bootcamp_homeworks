"""
    Abstract class exercise
"""

import abc


class Animal(abc.ABC):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def move(self):
        return f"{self.__class__.__name__}:"

    @abc.abstractmethod
    def make_noise(self):
        ...

    @abc.abstractmethod
    def eat(self):
        ...


class Lion(Animal):
    def move(self):
        return super().move() + "Tup, tup!"  

    def make_noise(self):
        return f"{self.__class__.__name__}: Roaaar!!!"

    def eat(self):
        return f"{self.__class__.__name__}: Mlasku, mlask!"


class Seal(Animal):
    def move(self):
        return "Plusk, plusk!"

    def make_noise(self):
        return "Ou ou ou"

    def eat(self):
        return "Mlasku, mlask!"


class Parrot(Animal):
    def move(self):
        return "Fruuu, fruuu!"

    def make_noise(self):
        return "Witajcie!"

    def eat(self):
        return "Dziob, dziob! Ale smaczne!"


class Zoo:
    def __init__(self, animals):
        self.animals = animals

    def open(self):
        for animal in self.animals:
            print(animal.move())
            print(animal.make_noise())

    def close(self):
        for animal in self.animals:
            print(animal.make_noise())
            print(animal.move())

    def feed_animals(self):
        for animal in self.animals:
            print(animal.make_noise())
            print(animal.eat())
            print(animal.make_noise())


lion = Lion("Leon")
seal = Seal("Zdzichu")
parrot = Parrot("Rychu")

zoo_krakow = Zoo([lion, seal, parrot])
zoo_krakow.open()
print("")
zoo_krakow.feed_animals()
print("")
zoo_krakow.close()
