from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .zone import Zone
    from .poi import PointOfInterest
    from typing import Dict, List, Optional
    from ..game_manager import GameManager

from ..entities import CommandReceiver

class PointOfInterest(CommandReceiver):

    def __init__(self, name: str, id : str) -> None:
        self._name = name
        self._id = id

    def get_name(self) -> str:
        return self._name

    def get_id(self) -> str:
        return self._id

    def receive_command(self, command: str, args: Dict[str, str], gm: GameManager):
        print(command)

    def __str__(self) -> str:
        return f"{self._name} ({self._id})"


class ZonePoI(PointOfInterest):
    def __init__(self, name: str, id : str, zone : Zone) -> None:
        super().__init__(name, id)
        self._zone = zone

    def get_zone(self) -> Zone:
        return self._zone

class ItemPoI(PointOfInterest):
    pass


class NPCPoI(PointOfInterest):
    pass


class Door(PointOfInterest):
    def __init__(self, name: str, locked: bool = True,
                 key_id: Optional[int] = None, pickable: bool = True):
        super().__init__(name)

        self._locked = locked
        self._requires_key = key_id != None
        self._key_id = key_id
        self._pickable = pickable



