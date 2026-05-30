import json


class StateManager:

    def __init__(self, state_file):

        self.state_file = state_file

    def save(self, data):

        with open(
            self.state_file,
            "w"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )

    def load(self):

        try:

            with open(
                self.state_file
            ) as f:

                return json.load(f)

        except FileNotFoundError:

            return {
                "completed": []
            }