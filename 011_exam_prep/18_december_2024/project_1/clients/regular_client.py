from project_3.clients.base_client import BaseClient


class RegularClient(BaseClient):
    MIN_ORDERS_CNT = 1
    MAX_DISCOUNT = 5.0
    MIN_DISCOUNT = 0.0

    def update_discount(self):
        if self.total_orders >= self.MIN_ORDERS_CNT:
            self.discount = self.MAX_DISCOUNT
        else:
            self.discount = self.MIN_DISCOUNT
        