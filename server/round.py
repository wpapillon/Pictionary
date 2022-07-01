import time as t
from _thread import *
from .game import Game
from .chat import Chat


class Round(object):
    def __init__(self, word, player_drawing, players, game):
        """
        init object
        :param word: str
        :param player_drawing:Player
        :param players: Player[]
        """
        self.word = word
        self.player_drawing = player_drawing
        self.player_guessed = []
        self.skips = 0
        self.player_scores = {player: 0 for player in players}
        self.time = 75
        self.start = t.time()
        self.chat = Chat(self)
        start_new_thread(self.time_thread(), ())
        
    def time_thread(self):
        """
        Runs in thread to keep track of time
        :return: None
        """
        while self.time > 0:
            t.sleep(1)
            self.time -= 1

        self.end_round("time is up")

    def guess(self, player, wrd):
        """

        :param player:Player
        :param wrd:str
        :return: boolean if player got guess correct
        """
        correct = wrd == self.word
        if correct:
            self.player_guessed.append(player)
            # TODO implement score system here

        return wrd == self.word

    def get_scores(self):
        """

        :return: all the player score
        """
        return self.scores()

    def get_score(self,player):
        """
        Gets a specific player scores
        :param player: Player
        :return: player's score
        """
        if player in self.player_scores:
            return self.player_scores[player]
        else:
            raise Exception("player does not exist in score list")

    def player_left(self, player):
        """
        remove players that left from scores and list
        :param player:Player
        :return:None
        """
        if player in self.player_scores:
            del self.player_scores[player]

        if player in self.player_guessed:
            self.player_guessed.remove(player)

        if player == self.player_drawing:
            self.end_round("drawing player leaves")

    def end_round(self, msg):
        # TODO implement end_round functionality here
        pass

    def skip(self):
        """
        Returns true if round skipped threshold met
        :return:bool
        """
        self.skips +=1
        if self.skips > len(self.player)-2:
            self.skips = 0
            return True
        return False
