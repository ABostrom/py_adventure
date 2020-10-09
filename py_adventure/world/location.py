from .zone import Zone

class Location:

    def __init__(self, name :str, zone : Zone) -> None:
        self._name = name
        self._zone = zone

    def get_name(self) -> str:
        return self._name

    def get_zone(self) -> Zone:
        return self._zone

    def __str__(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return str(self)

# subclass of location
class Building(Location):
    pass

    