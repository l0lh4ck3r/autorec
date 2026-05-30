import yaml

from pathlib import Path

from modules.subfinder import (
    SubfinderModule
)

from modules.dnsx import (
    DnsxModule
)

from modules.httpx_module import (
    HttpxModule
)

from modules.gau_module import GauModule
from modules.waybackurls_module import (
    WaybackUrlsModule
)

from modules.gowitness_module import (
    GowitnessModule
)


MODULE_MAP = {

    "subfinder": SubfinderModule,

    "dnsx": DnsxModule,

    "httpx": HttpxModule,

    "gau": GauModule,

    "waybackurls": WaybackUrlsModule,

    "gowitness": GowitnessModule
}


def load_modules(profile):

    config_file = (
        Path("config")
        / "profiles.yaml"
    )

    config = yaml.safe_load(
        config_file.read_text()
    )

    module_names = (
        config["profiles"]
        [profile]
        ["modules"]
    )

    modules = []

    for name in module_names:

        modules.append(
            MODULE_MAP[name]()
        )


    return modules