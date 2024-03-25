from ex_01.clients.base_client import BaseClient


class Adult (BaseClient):
    INTEREST = 4.0
    AVAILABLE_LOAN = "MortgageLoan"

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=self.INTEREST)

    def increase_clients_interest(self):
        self.interest += 2.0
