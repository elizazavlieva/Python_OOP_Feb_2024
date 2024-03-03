from typing import List
from project.animal import Animal
from project.worker import Worker
class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[str] = []
        self.workers: List[str] = []

    def add_animal(self, animal: str, price: int):
        capacity = len(self.animals) < self.__animal_capacity
        budget = price <= self.__budget
        if not capacity:
            return "Not enough space for animal"
        elif not budget:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker = [worker for worker in self.workers if worker.name == worker_name]
        if worker:
            self.workers.remove(worker[0])
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salary = sum(worker.salary for worker in self.workers)
        if self.__budget >= sum_salary:
            self.__budget -= sum_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        expense = sum(ex.money_for_care for ex in self.animals)
        if expense <= self.__budget:
            self.__budget -= expense
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        animals = {"Lions": [], "Tigers": [], "Cheetahs": []}
        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                animals["Lions"].append(animal)
            elif animal.__class__.__name__ == 'Tiger':
                animals["Tigers"].append(animal)
            elif animal.__class__.__name__ == "Cheetah":
                animals["Cheetahs"].append(animal)

        result = [f"You have {len(self.animals)} animals"]

        for creature, count in animals.items():
            result.append(f"----- {len(count)} {creature}:")
            result.append("\n".join([a.__repr__() for a in count]))

        return "\n".join(result)

    def workers_status(self):
        workers = {"Keepers": [], "Caretakers": [], "Vets": []}
        for worker in self.workers:
            if worker.__class__.__name__ == 'Keeper':
                workers["Keepers"].append(worker)
            elif worker.__class__.__name__ == 'Caretaker':
                workers["Caretakers"].append(worker)
            elif worker.__class__.__name__ == "Vet":
                workers["Vets"].append(worker)

        result = [f"You have {len(self.workers)} workers"]
        for staff, count in workers.items():
            result.append(f"----- {len(count)} {staff}:")
            result.append("\n".join([a.__repr__() for a in count]))

        return "\n".join(result)