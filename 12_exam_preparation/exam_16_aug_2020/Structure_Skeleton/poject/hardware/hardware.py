from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.used_memory = self.get_used_memory()
        self.used_capacity = self.get_used_capacity()

    def install(self, software: Software):
        capacity_left = abs(self.used_capacity - self.capacity)
        memory_left = abs(self.used_memory - self.memory)
        if capacity_left < software.capacity_consumption or memory_left < software.memory_consumption:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software: Software):
        self.software_components.remove(software)

    def get_used_memory(self):
        return sum(x.capacity_consumption for x in self.software_components)

    def get_used_capacity(self):
        return sum(x.memory_consumption for x in self.software_components)