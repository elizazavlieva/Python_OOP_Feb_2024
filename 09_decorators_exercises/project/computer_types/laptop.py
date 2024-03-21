import math

from project.computer_types.computer import Computer


class Laptop(Computer):
    PROCESSORS = {"AMD Ryzen 9 5950X": 900,
                  "Intel Core i9-11900H": 1050,
                  "Apple M1 Pro": 1200}

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")

        if ram not in [2**i for i in range(1, 8)]:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = math.log2(ram) * Computer.RAM_PRICE + self.PROCESSORS[processor]
        return self.create_computer()



