from __future__ import annotations
from collections import defaultdict, Counter
from typing import Counter, Set, ClassVar, Dict
from weakref import WeakValueDictionary

class Entity:
    # a list of all the current entities.
    entities : ClassVar[WeakValueDictionary] = WeakValueDictionary()
    entity_naming : ClassVar[Counter[str]] = Counter()

    def __init__(self, name) -> None:
        self._name = name 
        Entity.entity_naming.update([name])
        count = Entity.entity_naming[name]       
        if count > 1:
            self._name+= str(count-1)

        print(self._name)
        # add the entity to the entities map.
        Entity.entities[self._name] = self

    def get_name(self) -> str:
        return self._name

    def __del__(self) -> None:
        del Entity.entities[self._name]

        print("bye" + self._name)