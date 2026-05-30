from core.state import StateManager


class Engine:

    def __init__(
        self,
        modules
    ):
        self.modules = modules

    async def run(
        self,
        context
    ):

        state = StateManager(
            context.workspace
            / "state.json"
        )

        data = state.load()

        completed = set(
            data["completed"]
        )

        while (
            len(completed)
            < len(self.modules)
        ):

            for module in self.modules:

                if (
                    module.name
                    in completed
                ):
                    continue

                ready = all(
                    dep in completed
                    for dep
                    in module.dependencies
                )

                if ready:

                    print(
                        f"Running "
                        f"{module.name}"
                    )

                    await module.run(
                        context
                    )

                    completed.add(
                        module.name
                    )

                    state.save(
                        {
                            "completed":
                            list(completed)
                        }
                    )