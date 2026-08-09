from project.robots.base_robot import BaseRobot

class MaleRobot(BaseRobot):
    INITIAL_WEIGHT = 9
    WEIGHT_INCREASE = 3
    POSSIBLE_SERVICE = 'MainService'

    def __init__(self, name:str, kind:str, price:float):
        super().__init__(name, kind, price, weight=self.INITIAL_WEIGHT)

    def eating(self):
        self.INITIAL_WEIGHT += self.WEIGHT_INCREASE