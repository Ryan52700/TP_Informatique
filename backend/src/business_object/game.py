from enum import Enum

from player.py import Player
from Typing import datetime


class Game_mode_enum(Enum):
    COINFLIP = "coinflip"
    DICE = "dice"


class Game:

    def __init__(self, player1: Player, player2: Player, game_mode: Game_mode_enum, winner: Player | None, description: str, timestamp: datetime):
        self.id_game = None
        self.player1 = player1
        self.player2 = player2
        self.game_mode = game_mode
        self.winner = winner
        self.description = description
        self.timestamp = timestamp

    def __str__(self):
        """
        Fonction str
        """
        f"{self.game_mode} entre {self.player1} et {self.player2}. Gagnant : {self.winner}"
