from abc import ABC, abstractmethod


class ReconModule(ABC):

    name = ""

    dependencies = []

    @abstractmethod
    async def run(self, context):
        pass
