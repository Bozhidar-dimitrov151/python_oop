from project.services.base_service import BaseService


class MainService(BaseService):
    INITIAL_CAPACITY = 30

    def __init__(self, name:str):
        super().__init__(name, capacity=self.INITIAL_CAPACITY)

    def details(self):
        return f"""{self.name} Main Service:
Robots: {self._get_names()}"""