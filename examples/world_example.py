from py_adventure import ZoneConnection
from py_adventure import City, Zone, Location, Building
from py_adventure import World

from typing import Dict, List


gate : Location = Location("City Gate")
inn : Location = Building("Lion's Rest Inn")

city1 : Zone = City("Baldur's Gate", [gate,inn])
city2 : Zone = City("Elturel")

road1 : Zone = Zone("Fields of the Dead")

#exit from BG to Fields of the Dead
connection1 = ZoneConnection("North Exit", road1)
#region exits
connection2 = ZoneConnection("West Exit", city1)
connection3 = ZoneConnection("East Exit", city2)
#exit from elturel to region
connection4 = ZoneConnection("South Exit", road1)

connections : Dict[Zone, List[ZoneConnection]] = {
    city1 : [connection1],
    road1 : [connection2, connection3],
    city2 : [connection4]
}


world : World = World("Faerun", city1, connections)
print(world.get_name())

print(world.get_current_zone())

current_zone : Zone = world.get_current_zone()

for loc in current_zone.get_locations():
    print(loc)

print(world.get_available_exits())




print(world.__dict__)


