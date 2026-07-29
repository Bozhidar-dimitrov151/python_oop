from project_1.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    DEFAULT_OXYGEN_LEVEL = 540
    MISS_OXYGEN_PERCENT = 0.30

    def __init__(self, name: str, oxygen_level: int = DEFAULT_OXYGEN_LEVEL):
        super().__init__(name, oxygen_level)