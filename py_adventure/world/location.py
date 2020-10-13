from __future__ import annotations
from py_adventure.world.connection import ZoneConnection
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .zone import Zone
    from .poi import PointOfInterest
    from typing import Dict, List
    from ..game_manager import GameManager

from ..entities.command_receiver import CommandReceiver
from .poi import ZonePoI


class Location(CommandReceiver):

    def __init__(self, name: str, id : str, description : str, pois: List[PointOfInterest] = []) -> None:
        self._name = name
        self._points = pois
        self._id = id
        self._description = description

    def get_name(self) -> str:
        return self._name

    def get_id(self) -> str:
        return self._id

    def get_description(self)-> str:
        return self._description

    def set_zone(self, zone: Zone) -> None:
        self._zone = zone
        self._zone_poi = ZonePoI("Leave", "leave", self._zone) 

    def get_zone(self) -> Zone:
        return self._zone

    def get_points_of_interest(self) -> List[PointOfInterest]:
        return [self._zone_poi,*self._points]

    def __str__(self) -> str:
        return f"{self._name} ({self._id})"

    def receive_command(self, command: str, args: Dict[str, str], gm: GameManager) -> bool:
        if command == "goto":
            #match the argument to 
            if self._zone_poi.get_id() == args["parameters"]:
                gm.change_zone(self._zone_poi.get_zone())
                return True

        return False

    def get_valid_commands(self) -> List[str]:
        return ["goto"]


# subclass of location

class ZoneConnectionLocation(Location):
    def __init__(self, name: str, id : str, description : str, connection: ZoneConnection):
        super().__init__(name, id, description)
        self._connection = connection

    def get_zone(self) -> Zone:
        return self._connection._zone


class Building(Location):
    pass
