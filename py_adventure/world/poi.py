

class PointOfInterest:
    
    def __init__(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name

    def interact(self) -> bool:
        return False

class ItemPoI(PointOfInterest):
    pass

class NPCPoI(PointOfInterest):
    pass


class Door(PointOfInterest):
    pass