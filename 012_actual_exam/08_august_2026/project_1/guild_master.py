from project.guild_halls.combat_hall import CombatHall
from project.guild_halls.magic_tower import MagicTower
from project.guild_members.mage import Mage
from project.guild_members.warrior import Warrior
from project.guild_halls.base_guild_hall import BaseGuildHall


class GuildMaster:
    valid_members = {
        "Mage": Mage,
        "Warrior": Warrior
    }

    valid_halls = {
        "CombatHall": CombatHall,
        "MagicTower": MagicTower
    }

    def __init__(self):
        self.members = []
        self.guild_halls = []

    def add_member(self, member_type: str, member_tag: str, member_gold: int):
        if member_type not in self.valid_members:
            raise ValueError("Invalid member type!")

        for member in self.members:
            if member.tag == member_tag:
                raise ValueError(f"{member_tag} has already been added!")

        member = self.valid_members[member_type](member_tag, member_gold)

        self.members.append(member)

        return f"{member_tag} is successfully added as {member_type}."

    def add_guild_hall(self, guild_hall_type: str, guild_hall_alias: str):
        if guild_hall_type not in self.valid_halls:
            raise ValueError("Invalid guild hall type!")

        for guild_hall in self.guild_halls:
            if guild_hall.alias == guild_hall_alias:
                raise ValueError(f"{guild_hall_alias} has already been added!")

        guild_hall = self.valid_halls[guild_hall_type](guild_hall_alias)

        self.guild_halls.append(guild_hall)

        return f"{guild_hall_alias} is successfully added as a {guild_hall_type}."

    def assign_member(self, guild_hall_alias: str, member_type: str):
        guild_hall = None

        for hall in self.guild_halls:
            if hall.alias == guild_hall_alias:
                guild_hall = hall
                break

        if guild_hall is None:
            raise ValueError(f"Guild hall {guild_hall_alias} does not exist!")

        member = None

        for current_member in self.members:
            if current_member.role == member_type:
                member = current_member
                break

        if member is None:
            raise ValueError("No available members of the type!")

        if len(guild_hall.members) >= guild_hall.max_member_count:
            return "Maximum member count reached. Assignment is impossible."

        self.members.remove(member)
        guild_hall.members.append(member)

        return f"{member.tag} was assigned to {guild_hall_alias}."

    def practice_members(
            self,
            guild_hall: BaseGuildHall,
            sessions_number: int
    ):
        for _ in range(sessions_number):
            for member in guild_hall.members:
                member.practice()

        total_skill_level = sum(
            member.skill_level for member in guild_hall.members
        )

        return (
            f"{guild_hall.alias} members have "
            f"{total_skill_level} total skill level after "
            f"{sessions_number} practice session/s."
        )

    def unassign_member(
            self,
            guild_hall: BaseGuildHall,
            member_tag: str
    ):
        member = None

        for current_member in guild_hall.members:
            if current_member.tag == member_tag:
                member = current_member
                break

        if member is None or member.skill_level == 10:
            return "The unassignment process was canceled."

        guild_hall.members.remove(member)
        self.members.append(member)

        return f"Unassigned member {member_tag}."

    def guild_update(self, min_skill_level_value: int):
        for guild_hall in self.guild_halls:
            guild_hall.increase_gold(min_skill_level_value)

        sorted_halls = sorted(
            self.guild_halls,
            key=lambda hall: (-len(hall.members), hall.alias)
        )

        result = [
            "<<<Guild Updated Status>>>",
            f"Unassigned members count: {len(self.members)}",
            f"Guild halls count: {len(self.guild_halls)}"
        ]

        for guild_hall in sorted_halls:
            result.append(f">>>{guild_hall.status()}")

        return "\n".join(result)