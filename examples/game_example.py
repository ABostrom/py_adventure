


from py_adventure import *

barrel : PointOfInterest = PointOfInterest("Barrel", "barrel")

gate : Location = Location("City Gate", "gate", "A large city gate looms before you")
inn : Location = Building("Lion's Rest Inn", "inn", "A quaint and homely looking tavern", [barrel])

city1 : Zone = City("Baldur's Gate", "baldursgate", [gate,inn])
city2 : Zone = City("Elturel", "elturel", [])

road1 : Zone = Zone("Fields of the Dead", "fields", [])



#exit from BG to Fields of the Dead
connection1 = ZoneConnectionLocation("North Exit", "north", "Leads to the fields of the dead" ,road1)
city1.add_locations([connection1])

#region exits
connection2 = ZoneConnectionLocation("West Exit", "west", "Leads to the city of Baldur's Gate" ,city1)
connection3 = ZoneConnectionLocation("East Exit", "east", "Leads to the city of Elturel" ,city2)
road1.add_locations([connection2, connection3])

#exit from elturel to region
connection4 = ZoneConnectionLocation("South Exit", "south", "Leads to the fields of the dead" ,road1)
city2.add_locations([connection4])



my_world : Region = Region("Faerun", city1, [city1, road1, city2])

gm : GameManager = GameManager(my_world)

while True:
    gm.run()
