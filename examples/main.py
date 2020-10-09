from py_adventure import City, Zone
from py_adventure import World

from typing import Dict, List

city1 : Zone = City("Baldur's Gate")
city2 : Zone = City("Elturel")

connections : Dict[Zone, List[Zone]] = {
    city1 : [city2],
    city2 : [city1]
}

world : World = World("Faerun", connections)
print(world.get_name())




