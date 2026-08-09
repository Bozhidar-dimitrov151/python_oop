from project.services.base_service import BaseService


class SecondaryService(BaseService):
    INITIAL_CAPACITY = 15

    def __init__(self, name:str):
        super().__init__(name, capacity=self.INITIAL_CAPACITY)

    def details(self):
        return f"""{self.name} Secondary Service:
Robots: {self._get_names()}"""