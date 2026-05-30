from pathlib import Path


def latest_workspace():

    workspaces = list(
        Path("output")
        .glob("*")
    )

    workspaces.sort()

    return workspaces[-1]