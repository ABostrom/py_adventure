from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .zone import Zone
    from typing import List

class Region:
    
    def __init__(self, name :str, starting_zone: Zone, zones : List[Zone]) -> None:
        self._name = name
        self._current_zone = starting_zone
        self._zones = zones

        for zone in self._zones:
            zone.set_region(self)

    def get_name(self) -> str:
        return self._name

    def get_current_zone(self) -> Zone:
        return self._current_zone

    def __str__(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return str(self)
