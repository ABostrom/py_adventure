from py_adventure import PointOfInterest
from py_adventure import ZoneConnection
from py_adventure import City, Zone, Location, Building
from py_adventure import World

from typing import Dict, List



barrel : PointOfInterest = PointOfInterest("Barrel")

gate : Location = Location("City Gate")
inn : Location = Building("Lion's Rest Inn", [barrel])

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

current_zone : Zone = world.get_current_zone()
print(f"You arrive at {current_zone}")
print(f"Where would you like to explore?")
for loc in current_zone.get_locations():
    print(loc)

print("Or you can leave via:")
for connection in world.get_available_exits():
    print(connection)

print("--------------------------------")

#go to the lions rest inn.
current_location : Location = current_zone.get_locations()[1]
print(f"You arrive at the {current_location.get_name()}")

print("Looking around you notice:")
for poi in current_location.get_points_of_interest():
    print(poi.get_name())

print(f"or you can leave to go back to {current_zone}")






