
from py_adventure import *


sword : Item = Item("Sword", 1, 5.0, 10, "A plain sword")

print(sword)
print(sword.get_description())


key : Item = Item("Big Key", 2, quest_item=True, unique=True)

