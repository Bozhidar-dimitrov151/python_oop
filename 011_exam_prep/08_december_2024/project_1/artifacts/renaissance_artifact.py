from project_1.artifacts.base_artifact import BaseArtifact


class RenaissanceArtifact(BaseArtifact):
    ARTIFACT_TYPE = "Renaissance Artifact"

    def __init__(self, name: str, price: float, space_required: int):
        super().__init__(name, price, space_required)

    def artifact_information(self):
        return f"{self.ARTIFACT_TYPE}: {self.name}; Price: {self.price:.2f}; Required space: {self.space_required}"
