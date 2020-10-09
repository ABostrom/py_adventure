
#__all__ = ["World"]
from typing import Dict, List

from .zone import Zone

class World:
    
    def __init__(self, name :str, zones : Dict[Zone, List[Zone]]) -> None:
        self._name = name
        self._zones = zones

    def get_name(self) -> str:
        return self._name