import math

from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    PROCESSORS = {"AMD Ryzen 7 5700G": 500,
                  "Intel Core i5-12600K": 600,
                  "Apple M1 Max": 1800}

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.PROCESSORS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if ram not in [2**i for i in range(1, 8)]:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer { self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = math.log2(ram) * Computer.RAM_PRICE + self.PROCESSORS[processor]
        return self.create_computer()

