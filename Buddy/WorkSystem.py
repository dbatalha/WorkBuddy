import getpass


class WorkSystem:

    def __init__(self):
        pass

    @staticmethod
    def get_system_username():
        return getpass.getuser()
