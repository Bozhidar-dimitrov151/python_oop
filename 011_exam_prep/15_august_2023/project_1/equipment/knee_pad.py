from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    def __init__(self, protection:int, price:float):
        super().__init__(protection, price)

    def increase_price(self):
        self.price *= 1.20