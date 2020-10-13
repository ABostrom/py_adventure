from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..game_manager import GameManager

class CommandReceiver():

    def get_valid_commands(self) -> List[str]:
        return []

    def receive_command(self, command : str, args : Dict[str, str], gm: GameManager) -> bool:
        return False