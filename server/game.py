


class Game(object):

    def __init__(self, id, players):
        self.id = id
        self.players = []
        self.words_used = []
        self.round = None
        self.board = None

    def player_guess(self, player, guess):
        pass

    def player_disconnected(self, player):
        pass

    def skip(self):
        pass

    def update_score(self):
        pass

    def round_ended(self):
        pass

    def update_board(self, x, color):
        pass


