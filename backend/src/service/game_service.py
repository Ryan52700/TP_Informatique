import os  # ruff: ignore[unused-import]
import secrets  # ruff: ignore[unused-import]

from fastapi import HTTPException
from Typing import datetime

from business_object.game import Game
from business_object.game_mode import CoinFlipMode, DiceMode  # ruff: ignore[unused-import]
from business_object.game_mode_factory import GameModeFactory
from business_object.ScoringStrategy import update_player_ratings  # ruff: ignore[unused-import]
from dao.player_dao import PlayerDao
from utils.log_utils import log


class GameService:
    """Service that manages games."""

    @log
    def play(self, id_player: int, id_opponent: int, game_mode: str, **kwargs):
        """Executes a single round of a coin-flip game between two players.
        Args:
            id_player (int): The unique identifier of the first player.
            id_opponent (int): The unique identifier of the opponent.
            choice (str, optional): The player's choice ('heads' or 'tails'). Defaults to "heads".
        Returns:
            dict: A dictionary containing the match details and new elo
        Raises:
            HTTPException: 400 if the two players are the same.
            HTTPException: 404 if one or both players are not found in the database.
        """
        if id_player == id_opponent:
            raise HTTPException(status_code=400, detail="Two different players required")

        p1 = PlayerDao().find_by_id(id_player)
        p2 = PlayerDao().find_by_id(id_opponent)

        if not p1 or not p2:
            raise HTTPException(status_code=404, detail="Player not found")

        mode_de_jeu = GameModeFactory.get_mode(game_mode)
        partie = mode_de_jeu.play(id_player, id_opponent, kwargs)
        update_player_ratings(partie)

        PlayerDao().update(p1)
        PlayerDao().update(p2)

        return Game(partie.player1, partie.player2, partie.game_mode, partie.winner, partie.descrption, partie.timestamp)
