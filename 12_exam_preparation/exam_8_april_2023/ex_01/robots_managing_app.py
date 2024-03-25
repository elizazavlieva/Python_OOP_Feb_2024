from ex_01.robots.female_robot import FemaleRobot
from ex_01.robots.male_robot import MaleRobot
from ex_01.services.main_service import MainService
from ex_01.services.secondary_service import SecondaryService


class RobotsManagingApp:

    SERVICE_TYPES = {"MainService": MainService,
                     "SecondaryService": SecondaryService}
    ROBOT_TYPES = {"MaleRobot": MaleRobot,
                   "FemaleRobot": FemaleRobot}
    def __init__(self):
        self.robots = []
        self.services = []

    def get_robot(self, robot_name):
        return next((r for r in self.robots if r.name == robot_name), None)

    def get_service(self, service_name):
        return next((s for s in self.services if s.name == service_name), None)


    def add_service(self, service_type: str, name: str):
        if service_type not in self.SERVICE_TYPES:
            raise Exception("Invalid service type!")

        self.services.append(self.SERVICE_TYPES[service_type](name))
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.ROBOT_TYPES:
            raise Exception("Invalid robot type!")

        self.robots.append(self.ROBOT_TYPES[robot_type](name, kind, price))
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.get_robot(robot_name)
        service = self.get_service(service_name)

        if service.__class__.__name__ != robot.AVAILABLE_SERVICE:
            return "Unsuitable service."

        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        service.robots.append(robot)
        self.robots.remove(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):

        service = self.get_service(service_name)
        robot = next((r for r in service.robots if r.name == robot_name), None)

        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.get_service(service_name)

        fed_robots = len([r.eating() for r in service.robots])
        return f"Robots fed: {fed_robots}."

    def service_price(self, service_name: str):
        service = self.get_service(service_name)
        total_price = sum([r.price for r in service.robots])
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        service_result = [service.details() for service in self.services]

        return "\n".join(service_result)