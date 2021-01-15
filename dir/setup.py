from dir.auth import Authentication


class SetupFile:

    def __init__(self):
        self.auth = Authentication()
        self.auth.show()
