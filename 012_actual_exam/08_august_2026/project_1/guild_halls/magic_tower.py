from project.guild_halls.base_guild_hall import BaseGuildHall


class MagicTower(BaseGuildHall):
    MAX_MEMBER_COUNT = 4

    def __init__(self, alias:str):
        super().__init__(alias)

    def increase_gold(self, min_skill_level_value : int):
        for member in self.members:
            if member.role == "Mage" and member.skill_level >= min_skill_level_value:
                member.gold *= 2

    @property
    def max_member_count(self):
        return self.MAX_MEMBER_COUNT
