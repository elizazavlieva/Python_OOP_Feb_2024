from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    FOOD_TYPES = {
        "Bread": Bread,
        "Cake": Cake
    }
    DRINK_TYPES = {
        "Tea": Tea,
        "Water": Water
    }
    TABLE_TYPES = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable
    }

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type not in self.FOOD_TYPES:
            return
        if name in [x.name for x in self.food_menu]:
            raise Exception(f"{food_type} {name} is already in the menu!")

        self.food_menu.append(self.FOOD_TYPES[food_type](name, price))
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand:str):
        if drink_type not in self.DRINK_TYPES:
            return
        if name in [x.name for x in self.drinks_menu]:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        self.drinks_menu.append(self.DRINK_TYPES[drink_type](name, portion, brand))
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type not in self.TABLE_TYPES:
            return
        if self.get_table(table_number):
            raise Exception(f"Table {table_number} is already in the bakery!")
        self.tables_repository.append(self.TABLE_TYPES[table_type](table_number, capacity))
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        tables = [x for x in self.tables_repository if x.capacity >= number_of_people and not x.is_reserved]
        if not tables:
            return f"No available table for {number_of_people} people"
        tables[0].reserve(number_of_people)
        return f"Table {tables[0].table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        table = self.get_table(table_number)
        if not table:
            return f"Could not find table {table_number}"
        return self.make_order("Food", table, args)

    def order_drink(self, table_number: int, *args):
        table = self.get_table(table_number)
        if not table:
            return f"Could not find table {table_number}"
        return self.make_order("Drink", table, args)

    def leave_table(self, table_number: int):
        table = self.get_table(table_number)

        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f"Table: {table_number}\n" \
               f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        tables_info = []
        for table in self.tables_repository:
            info = table.free_table_info()
            if info:
                tables_info.append(info)
        return "\n".join(tables_info)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def get_table(self, table_number):
        return next(filter(lambda x: x.table_number == table_number, self.tables_repository), None)

    def make_order(self, items_type, table, items):
        items_in_menu = []
        items_not_in_menu = []
        for item in items:
            if items_type == "Food":
                obj = [x for x in self.food_menu if x.name == item]
                if obj:
                    items_in_menu.append(obj[0])
                    table.order_food(obj[0])
                else:
                    items_not_in_menu.append(item)
            elif items_type == "Drink":
                obj = [x for x in self.drinks_menu if x.name == item]
                if obj:
                    items_in_menu.append(obj[0])
                    table.order_drink(obj[0])
                else:
                    items_not_in_menu.append(item)
        result = [f"Table {table.table_number} ordered:"]
        [result.append(repr(obj)) for obj in items_in_menu]
        result.append(f"{self.name} does not have in the menu:")
        result.extend(items_not_in_menu)

        return "\n".join(result)
