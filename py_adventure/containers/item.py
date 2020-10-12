from .. import Entity


class Item (Entity):

    # TODO: review value and maybe make money class.
    def __init__(self, name: str, id: int, weight: float =0.1, 
                 value: int = 0, description: str = "", 
                 unique: bool = False, quest_item: bool = False) -> None:
        super().__init__(name)

        self._id: int = id
        self._weight: float = weight
        self._value: int = value
        self._desc: str = description
        self._unique : bool = unique
        self._quest_item : bool = quest_item

    def __str__(self) -> str:
        return f"{self._name}\nWeight:\t\t{self._weight}\nGold Value:\t{self._value}"

    def get_description(self):
        return self._desc
