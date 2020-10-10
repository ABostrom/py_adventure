from . import zone
from .poi import PointOfInterest
from typing import List


class Location:

    def __init__(self, name: str, pois: List[PointOfInterest] = []) -> None:
        self._name = name
        self._points = pois

    def get_name(self) -> str:
        return self._name

    def set_zone(self, zone: 'zone.Zone') -> None:
        self._zone = zone

    def get_zone(self) -> 'zone.Zone':
        return self._zone

    def __str__(self) -> str:
        return self._name


# subclass of location


class Building(Location):
    pass
