from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Game:
    """Représente une partie jouée entre deux joueurs."""
    player1: str
    player2: str
    winner: Optional[str]  
    score_player1: int
    score_player2: int
    mode: str             
    date: datetime = datetime.now()  
    