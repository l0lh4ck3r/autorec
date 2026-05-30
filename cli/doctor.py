import shutil


TOOLS = [

    "subfinder",
    "dnsx",
    "httpx",
    "naabu",
    "katana"
]


def doctor():

    print()

    for tool in TOOLS:

        if shutil.which(tool):

            print(
                f"[OK] {tool}"
            )

        else:

            print(
                f"[MISSING] {tool}"
            )