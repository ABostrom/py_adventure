

class Zone:

    def __init__(self, name :str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name

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



