



class Zone:

    def __init__(self, name :str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name


#subclasses of Zone. City and Forest.
class City (Zone):
    pass

class Forest (Zone):
    pass

