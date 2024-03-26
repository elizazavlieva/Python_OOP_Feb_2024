from ex_01.booths.open_booth import OpenBooth
from ex_01.booths.private_booth import PrivateBooth
from ex_01.delicacies.gingerbread import Gingerbread
from ex_01.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACY_TYPES = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen
    }
    BOOTH_TYPES = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth
    }

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def get_delicacy(self, delicacy_name):
        return next((d for d in self.delicacies if  d.name == delicacy_name), None)

    def get_booth(self, booth_number):
        return next((b for b in self.booths if b.booth_number == booth_number), None)

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in self.DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if name in [d.name for d in self.delicacies]:
            raise Exception(f"{name} already exists!")

        self.delicacies.append(self.DELICACY_TYPES[type_delicacy](name, price))
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if booth_number in [b.booth_number for b in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        self.booths.append(self.BOOTH_TYPES[type_booth](booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):

        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.get_booth(booth_number)
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = self.get_delicacy(delicacy_name)
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.get_booth(booth_number)
        bill = booth.price_for_reservation + sum(d.price for d in booth.delicacy_orders)
        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0.0
        self.income += bill
        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
