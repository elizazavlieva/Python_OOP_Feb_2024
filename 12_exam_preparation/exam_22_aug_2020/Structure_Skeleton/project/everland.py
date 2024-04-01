from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        return f"Monthly consumption: {self.expenses():.2f}$."

    def pay(self):
        info = []
        must_leave = []
        for room in self.rooms:
            total_expenses = room.expenses + room.room_cost
            if room.budget >= total_expenses:
                room.budget -= total_expenses
                info.append(f"{room.family_name} paid {(total_expenses):.2f}$ "
                            f"and have {room.budget:.2f}$ left." )
            else:
                info.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                must_leave.append(room)
        self.rooms = [rooms for rooms in self.rooms if rooms not in must_leave]
        return "\n".join(info)

    def status(self):
        hotel_info = [f"Total population: {sum(r.members_count for r in self.rooms)}"]

        for room in self.rooms:
            hotel_info.append(f"{room.family_name} with {room.members_count} members. "
                              f"Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            if room.children:
                for n, child in enumerate(room.children):
                    hotel_info.append(f"--- Child {n + 1} monthly cost: {child. get_monthly_expense():.2f}$")
            total_appliance = sum([appliance.get_monthly_expense() for appliance in room.appliances])
            hotel_info.append(f"--- Appliances monthly cost: {total_appliance:.2f}$")

        return "\n".join(hotel_info)

    def expenses(self):
        return sum([room.room_cost + room.expenses for room in self.rooms])