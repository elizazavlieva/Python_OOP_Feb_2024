from math import floor

from project.software.software import Software


class ExpressSoftware (Software):
    SOFTWARE_TYPE = "Express"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self.SOFTWARE_TYPE, capacity_consumption,
                         memory_consumption * 2)
