from ex_01.route import Route
from ex_01.user import User
from ex_01.vehicles.cargo_van import CargoVan
from ex_01.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VEHICLE_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if driving_license_number in [u.driving_license_number for u in self.users]:
            return f"{driving_license_number} has already been registered to our platform."

        self.users.append(User(first_name, last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if license_plate_number in [v.license_plate_number for v in self.vehicles]:
            return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(self.VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number))
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_id = len(self.routes) + 1
        route = next((r for r in self.routes if r.start_point == start_point and r.end_point == end_point), None)
        if route:
            if route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            else:
                route.is_locked = True

        self.routes.append(Route(start_point, end_point, length, route_id))
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = [user for user in self.users if user.driving_license_number == driving_license_number][0]
        vehicle = [vehicle for vehicle in self.vehicles if vehicle.license_plate_number == license_plate_number][0]
        route = [route for route in self.routes if route.route_id == route_id][0]

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self,count: int):
        vehicle_for_repairing = [v for v in self.vehicles if v.is_damaged]
        sorted_vehicle = sorted(vehicle_for_repairing, key=lambda x: (x.brand, x.model))[:count]

        for vehicle in sorted_vehicle:
            vehicle.change_status()
            vehicle.recharge()

        return f"{len(sorted_vehicle)} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda x: -x.rating)
        user_info = ["*** E-Drive-Rent ***"]
        [user_info.append(str(user)) for user in sorted_users]

        return "\n".join(user_info)