from hub.bot import Bot

class RandomBot(Bot):
    def __init__(self):
        print('random bot has been initialized')

    def make_action(self, state : dict) -> dict:
        pass