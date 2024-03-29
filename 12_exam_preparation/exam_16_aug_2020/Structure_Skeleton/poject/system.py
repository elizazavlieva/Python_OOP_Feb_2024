from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:

    _software = []
    _hardware = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = next(filter(lambda x: x.name == hardware_name, System._hardware), None)
        if not hardware:
            return "Hardware does not exist"

        new_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_software)
        System._software.append(new_software)


    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = next(filter(lambda x: x.name == hardware_name, System._hardware), None)
        if not hardware:
            return "Hardware does not exist"
        software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = next(filter(lambda x: x.name == hardware_name, System._hardware), None)
        software = next(filter(lambda x: x.name == software_name, System._software), None)
        if not hardware or not software:
            return f"Some of the components do not exist"
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        total_memory_consumption = sum([x.memory_consumption for x in System._software])
        total_capacity_consumption = sum(x.capacity_consumption for x in System._software)
        total_capacity = sum(x.capacity for x in System._hardware)
        total_memory = sum(x.memory for x in System._hardware)
        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {total_memory_consumption} / {total_memory}\n" \
               f"Total Capacity Taken: {total_capacity_consumption} / {total_capacity}"

    @staticmethod
    def system_split():
        result = []
        for hardware in System._hardware:
            express_components = len([x for x in hardware.software_components if x.software_type == "Express"])
            light_components = len([x for x in hardware.software_components if x.software_type == "Light"])
            used_memory = sum(x.memory_consumption for x in hardware.software_components)
            used_capacity = sum(x.capacity_consumption for x in hardware.software_components)
            software_components = ", ".join(x.name for x in hardware.software_components) \
                if hardware.software_components else "None"

            result.append(f'Hardware Component - {hardware.name}\n'
                          f'Express Software Components: {express_components}\n'
                          f'Light Software Components: {light_components}\n'
                          f'Memory Usage: {used_memory} / {hardware.memory}\n'
                          f'Capacity Usage: {used_capacity} / {hardware.capacity}\n'
                          f'Type: {hardware.hardware_type}\n'
                          f'Software Components: {software_components}')
        return "\n".join(result)

