from project_3.clients.base_client import BaseClient


class BusinessClient(BaseClient):
    MIN_ORDERS_CNT = 2
    MAX_DISCOUNT = 10.0
    MIN_DISCOUNT = 0.0

    def update_discount(self):
        if self.total_orders >= self.MIN_ORDERS_CNT:
            self.discount = self.MAX_DISCOUNT
        else:
            self.discount = self.MIN_DISCOUNT
