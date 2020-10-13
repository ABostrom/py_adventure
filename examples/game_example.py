


from py_adventure import *

barrel : PointOfInterest = PointOfInterest("Barrel", "barrel")

gate : Location = Location("City Gate", "gate", "A large city gate looms before you")
inn : Location = Building("Lion's Rest Inn", "inn", "A quaint and homely looking tavern", [barrel])

city1 : Zone = City("Baldur's Gate", "baldursgate", [gate,inn])
city2 : Zone = City("Elturel", "elturel")

road1 : Zone = Zone("Fields of the Dead", "fields")

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


my_world : Region = Region("Faerun", city1, connections)

gm : GameManager = GameManager(my_world)

while True:
    gm.run()
