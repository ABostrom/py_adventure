from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .location import Location
    from typing import Dict, List
    from ..game_manager import GameManager
    from .region import Region

from ..entities import CommandReceiver

class Zone(CommandReceiver):

    def __init__(self, name :str, id :str, locations :List[Location]) -> None:
        self._name = name
        self._locations = locations
        self._id = id

        #assign each location to this zone
        for loc in self._locations:
            loc.set_zone(self)

    def get_name(self) -> str:
        return self._name

    def get_id(self) -> str:
        return self._id

    def set_region(self, region : Region):
        self._region = region

    def get_locations(self) -> List[Location]:
        return self._locations

    def __str__(self) -> str:
        return f"{self._name} ({self._id})"

    def __repr__(self) -> str:
        return str(self)

    def add_locations(self, locations: List[Zone]) -> None:
        self._locations.extend(locations)

    def receive_command(self, command: str, args: Dict[str, str], gm: GameManager) -> bool:
        if command == "goto":
            #match the argument to 
            for loc in self.get_locations():
                if loc.get_id() == args["parameters"]:
                    gm.change_location(loc)
                    return True

        return False

    def get_valid_commands(self) -> List[str]:
        return ["goto"]



#subclasses of Zone. City and Forest.
class City (Zone):
    pass

class Road(Zone):
    pass

class Forest (Zone):
    pass

