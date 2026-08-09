from abc import ABC, abstractmethod

class BaseGuildHall(ABC):
    def __init__(self, alias: str):
        self.alias = alias
        self.members = []

    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, value):
        if not value.replace(" ", "").isalpha() or len(value.strip()) < 2:
            raise ValueError("Guild hall alias is invalid!")

        self.__alias = value

    @property
    @abstractmethod
    def max_member_count(self):
        pass

    def calculate_total_gold(self):
        return sum(member.gold for member in self.members)

    def status(self):
        member_tags = sorted(member.tag for member in self.members)

        if member_tags:
            members = " *".join(member_tags)
        else:
            members = "N/A"

        return (
            f"Guild hall: {self.alias}; "
            f"Members: {members}; "
            f"Total gold: {self.calculate_total_gold()}"
        )

    @abstractmethod
    def increase_gold(self, min_skill_level_value : int):
        pass