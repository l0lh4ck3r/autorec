from core.module import ReconModule


class TestModule(ReconModule):

    name = "test"

    async def run(self, context):

        print(
            f"Target: {context.target}"
        )
