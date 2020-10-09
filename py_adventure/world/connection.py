from .zone import Zone


class ZoneConnection:

    def __init__(self, name :str, zone :Zone) -> None:
        self._name = name
        self._zone = zone

    def __str__(self) -> str:
        return f"Take the {self._name } to get to {self._zone.get_name()}"

    def __repr__(self) -> str:
        return str(self)