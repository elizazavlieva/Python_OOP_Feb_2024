from project.animals.animal import Bird
from project.food import Food


class Owl(Bird):
    weight_per_food = 0.25
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)


    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food: Food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * Owl.weight_per_food


class Hen(Bird):
    weight_per_food = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        self.food_eaten += food.quantity
        self.weight += food.quantity * Hen.weight_per_food



