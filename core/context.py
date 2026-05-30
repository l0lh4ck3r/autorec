class ScanContext:

    def __init__(
        self,
        target,
        profile,
        workspace,
        repository,
        eventbus,
        scan_id=None
    ):
        self.target = target
        self.profile = profile
        self.workspace = workspace
        self.repository = repository
        self.eventbus = eventbus
        self.scan_id = scan_id

        self.data = {}