
#__all__ = ["World"]
from .zone import Zone
from .connection import ZoneConnection
from typing import Dict, List

class World:
    
    def __init__(self, name :str, starting_zone: Zone, zones : Dict[Zone, List[ZoneConnection]]) -> None:
        self._name = name
        self._zones = zones
        self._current_zone = starting_zone

    def get_name(self) -> str:
        return self._name

    def get_current_zone(self) -> Zone:
        return self._current_zone

    def get_available_exits(self) -> List[ZoneConnection]:
        return self._zones[self._current_zone]


    def __str__(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return str(self)
