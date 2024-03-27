from ex_01.client import Client
from ex_01.meals.meal import Meal


class FoodOrdersApp:
    MEAL_TYPES = ["Starter", "MainDish", "Dessert"]

    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 0

    def clear_order_info(self, client, canceled_order: bool = False):
        if canceled_order:
            self.return_meals_to_menu(client)
        client.order_with_quantity = {}
        client.shopping_cart = []
        client.bill = 0.0

    def return_meals_to_menu(self, client):
        for meal in self.menu:
            if meal in client.order_with_quantity:
                meal.quantity += client.order_with_quantity[meal]

    def get_meal(self, name):
        return next((m for m in self.menu if m.name == name), None)

    def get_client(self, phone_number):
        return next((c for c in self.clients_list if c.phone_number == phone_number), None)

    def register_client(self, client_phone_number: str):
        if client_phone_number in [c.phone_number for c in self.clients_list]:
            raise Exception("The client has already been registered!")

        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        [self.menu.append(m) for m in meals if type(m).__name__ in self.MEAL_TYPES]

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return "\n".join([m.details() for m in self.menu])

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        if not self.get_client(client_phone_number):
            self.register_client(client_phone_number)

        client = self.get_client(client_phone_number)

        for meal, qnty in meal_names_and_quantities.items():
            meal_obj = self.get_meal(meal)
            if not meal_obj:
                self.clear_order_info(client, True)
                raise Exception(f"{meal} is not on the menu!")

            if meal_obj.quantity < qnty:
                self.clear_order_info(client, True)
                raise Exception(f"Not enough quantity of {type(meal_obj).__name__}: {meal_obj.name}!")

            client.shopping_cart.append(meal_obj)
            meal_obj.quantity -= qnty
            client.bill += qnty * meal_obj.price
            if meal_obj not in client.order_with_quantity:
                client.order_with_quantity[meal_obj] = 0
            client.order_with_quantity[meal_obj] += qnty
        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join([m.name for m in client.shopping_cart])} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.get_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        self.clear_order_info(client, True)
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.get_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        total_paid_money = client.bill
        self.receipt_id += 1
        self.clear_order_info(client)
        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} " \
               f"was successfully paid for {client.phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."