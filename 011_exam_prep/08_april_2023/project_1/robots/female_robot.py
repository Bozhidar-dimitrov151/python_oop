from project.robots.base_robot import BaseRobot

class FemaleRobot(BaseRobot):
    INITIAL_WEIGHT = 7
    WEIGHT_INCREASE = 1
    POSSIBLE_SERVICE = 'SecondaryService'

    def __init__(self, name:str, kind:str, price:float):
        super().__init__(name, kind, price, weight=self.INITIAL_WEIGHT)

    def eating(self):
        self.INITIAL_WEIGHT += self.WEIGHT_INCREASE