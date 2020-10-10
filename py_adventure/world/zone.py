from py_adventure.world import location
from typing import List, Optional

class Zone:

    def __init__(self, name :str, locations :List['location.Location'] = []) -> None:
        self._name = name
        self._locations = locations

        #assign each location to this zone
        for loc in self._locations:
            loc.set_zone(self)

    def get_name(self) -> str:
        return self._name

    def get_locations(self) -> List['location.Location']:
        return self._locations

    def __str__(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return str(self)

#subclasses of Zone. City and Forest.
class City (Zone):
    pass

class Road(Zone):
    pass

class Forest (Zone):
    pass

