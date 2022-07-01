from .game import Game


class Player(object):
    def __init__(self, ip, name):
        """
        Init the player object
        :param ip: str
        :param name: str
        """
        self.game = None
        self.ip=ip
        self.name = name
        self.score = 0

    def set_game(self, game):
        """
        Sets the players game association
        :param game: Game
        :return: None
        """
        self.game = game

    def update_score(self, new_score):
        """
        Updates player score
        :param new_score: int
        :return:None
        """
        self.score += new_score

    def guess(self, wrd):
        """
        makes a player guess
        :param wrd: string
        :return: bool
        """
        return self.game.player_guess(self, wrd)

    def disconnect(self):
        """
        Call to disconnect player
        :return:
        """
        pass

    def get_score(self):
        """
        Get the player score
        :return: int
        """
        return self.score

    def get_name(self):
        """
        Gets the player name
        :return: str
        """
        return self.name

    def get_ip(self):
        """
        Gets player ip address
        :return: string
        """
        return  self.ip
