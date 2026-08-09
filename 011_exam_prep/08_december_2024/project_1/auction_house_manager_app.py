from project_1.artifacts.renaissance_artifact import RenaissanceArtifact
from project_1.artifacts.contemporary_artifact import ContemporaryArtifact
from project_1.collectors.private_collector import PrivateCollector
from project_1.collectors.museum import Museum

class AuctionHouseManagerApp:
    VALID_ARTIFACTS = {
        "RenaissanceArtifact" : RenaissanceArtifact,
        "ContemporaryArtifact" : ContemporaryArtifact
    }

    VALID_COLLECTORS = {
        "PrivateCollector" : PrivateCollector,
        "Museum" : Museum
    }
    @staticmethod
    def _find_obj_by_name(obj_name, collection):
        return next((obj for obj in collection if obj.name == obj_name), None)

    def __init__(self):
        self.artifacts = []
        self.collectors = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):

        if artifact_type not in self.VALID_ARTIFACTS:
            raise ValueError("Unknown artifact type!")

        if self._find_obj_by_name(artifact_name, self.artifacts) is not None:
            raise ValueError(f"{artifact_name} has been already registered!")

        new_artifact = self.VALID_ARTIFACTS[artifact_type](
            artifact_name, artifact_price, artifact_space
        )
        self.artifacts.append(new_artifact)

        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):

        if collector_type not in self.VALID_COLLECTORS:
            raise ValueError("Unknown collector type!")

        if self._find_obj_by_name(collector_name, self.collectors) is not None:
            raise ValueError(f"{collector_name} has been already registered!")

        new_collector = self.VALID_COLLECTORS[collector_type](collector_name)

        self.collectors.append(new_collector)

        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):

        collector = self._find_obj_by_name(collector_name, self.collectors)
        if collector is None:
            raise ValueError(
                f"Collector {collector_name} is not registered to the auction!"
            )

        artifact = self._find_obj_by_name(artifact_name, self.artifacts)
        if artifact is None:
            raise ValueError(
                f"Artifact {artifact_name} is not registered to the auction!"
            )

        if not collector.can_purchase(artifact.price, artifact.space_required):
            return "Purchase is impossible."

        self.artifacts.remove(artifact)
        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required
        return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."

    def remove_artifact(self, artifact_name: str):
        artifact = self._find_obj_by_name(artifact_name, self.artifacts)

        if artifact is None:
            return "No such artifact."

        artifact_info = artifact.artifact_information()
        self.artifacts.remove(artifact)
        return f"Removed {artifact_info}"

    def fundraising_campaigns(self, max_money: float):

        count = len([c.increase_money() for c in self.collectors if c.available_money <= max_money])

        return f"{count} collector/s increased their available money."
    def get_auction_report(self):

        collectors = sorted(
            self.collectors,
            key=lambda c: (-len(c.purchased_artifacts), c.name),
        )
        count_of_sold_artifacts = sum(len(c.purchased_artifacts) for c in self.collectors)
        result = ["**Auction statistics**",
                  f"Total number of sold artifacts: {count_of_sold_artifacts}",
                  f"Available artifacts for sale: {len(self.artifacts)}",
                  "***"]

        [result.append(str(c)) for c in collectors]

        return "\n".join(result)
