from project.animals.animal import Mammal
from project.food import Food


class Mouse(Mammal):
    weight_per_food = 0.10

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    @staticmethod
    def food_preferences():
        return ["Vegetable", "Fruit"]

    def feed(self, food: Food):
        if food.__class__.__name__ not in self.food_preferences():
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * Mouse.weight_per_food


class Dog(Mammal):
    weight_per_food = 0.40

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * Dog.weight_per_food


class Cat(Mammal):
    weight_per_food = 0.30

    def make_sound(self):
        return "Meow"

    @staticmethod
    def food_preferences():
        return ["Vegetable", "Meat"]

    def feed(self, food: Food):
        if food.__class__.__name__ not in self.food_preferences():
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * Cat.weight_per_food


class Tiger(Mammal):
    weight_per_food = 1

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * Tiger.weight_per_food
