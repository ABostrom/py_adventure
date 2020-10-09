from .zone import Zone

class Location:

    def __init__(self, name :str, zone : Zone):
        self._name = name
        self._zone = zone

    def get_name(self) -> str:
        return self._name

    def get_zone(self) -> Zone:
        return self._zone

# subclass of location
class Building(Location):
    pass

    