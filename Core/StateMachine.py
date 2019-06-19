__author__ = 'Daniel Batalha'


class StateMachine(object):
    def __init__(self):
        self.saved_state = None

    def get_state(self):
        return self.saved_state

    def run(self, state):
        self.saved_state = state
