import os  # ruff: ignore[unused-import]
import secrets
from abc import ABC, abstractmethod
from random import randint

from fastapi import HTTPException  # ruff: ignore[unused-import]
from game import Game
from Typing import datetime

from dao.player_dao import PlayerDao  # ruff: ignore[unused-import]
from utils.log_utils import log  # ruff: ignore[unused-import]


class GameMode(ABC):

    @abstractmethod
    def play(self, p1, p2):
        pass


class DiceMode(GameMode):

    def play(self, p1, p2):
        score1 = randint(1, 6)
        score2 = randint(1, 6)
        if score1 == score2:
            return Game(p1, p2, "dice", None, "Jeté de dé, le joueur avec le plus haut score gagne", datetime.datetime.now())
        elif score1 > score2:
            return Game(p1, p2, "dice", p1, "Jeté de dé, le joueur avec le plus haut score gagne", datetime.datetime.now())
        else:
            return Game(p1, p2, "dice", p2, "Jeté de dés", datetime.datetime.now())


class CoinFlipMode(GameMode):

    def play(self, p1, p2, choice="heads"):

        result = secrets.choice(["heads", "tails"])
        winner = p1 if result == choice else p2

        return Game(p1, p2, "coinflip", winner.username, "Pile ou face", datetime.datetime.now())
