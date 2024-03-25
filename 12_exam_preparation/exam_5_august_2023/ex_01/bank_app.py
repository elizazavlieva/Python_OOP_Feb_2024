from ex_01.clients.adult import Adult
from ex_01.clients.student import Student
from ex_01.loans.mortgage_loan import MortgageLoan
from ex_01.loans.student_loan import StudentLoan


class BankApp:
    LOAN_TYPES = {"StudentLoan": StudentLoan,
                  "MortgageLoan": MortgageLoan}

    CLIENT_TYPES = {"Student": Student,
                    "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type):
        if loan_type not in self.LOAN_TYPES:
            raise Exception("Invalid loan type!")

        self.loans.append(self.LOAN_TYPES[loan_type]())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENT_TYPES:
            raise Exception("Invalid client type!")
        if self.capacity <= len(self.clients):
            return f"Not enough bank capacity."

        self.clients.append(self.CLIENT_TYPES[client_type](client_name, client_id, income))
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self.get_client(client_id)
        loan = self.get_loan(loan_type) # possible error

        if type(loan).__name__ != client.AVAILABLE_LOAN:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self.get_client(client_id)
        if not client:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        count = len([l.increase_interest_rate() for l in self.loans if type(l).__name__ == loan_type])
        return f"Successfully changed {count} loans."

    def increase_clients_interest(self, min_rate: float):
        count = len([c.increase_clients_interest() for c in self.clients if c.interest < min_rate])
        return f"Number of clients affected: {count}."

    def get_statistics(self):
        income = sum([c.income for c in self.clients])
        granted_sum = sum([sum([l.amount for l in client.loans]) for client in self.clients])
        avg_client_interest_rate = sum([c.interest for c in self.clients]) / len(self.clients) if self.clients else 0

        return f"Active Clients: {len(self.clients)}\n" \
               f"Total Income: {income:.2f}\n" \
               f"Granted Loans: {sum([len(c.loans) for c in self.clients])}, Total Sum: {granted_sum:.2f}\n" \
               f"Available Loans: {len(self.loans)}, Total Sum: {sum([l.amount for l in self.loans]):.2f}\n" \
               f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"


    def get_loan(self, loan_type):
        return next((l for l in self.loans if type(l).__name__ == loan_type), None)

    def get_client(self, client_id):
        return next((c for c in self.clients if c.client_id == client_id), None)