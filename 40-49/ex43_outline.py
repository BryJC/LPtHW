####################
#GAME CONCEPT
"""Aliens have invaded a space ship and our hero has to go through a maze of rooms defeating them so he can escape into an escape pd to the planet below. The game will be more like a Zork or Adventure type of game with text outputs and funny ways to die. The game will involve an engine that runs a map full of rooms or scenes. Each rom will print its own description when the player enters it and then tell the engine what room to run next out of the map"""
#DESCRIPTIONS(Scenes == Story)
"""
Death:
    This is when the player dies and should be something funny.
Central Corridor:
    This is the starting point and has a Gothon already standing there that the player has to defeat with a jke before continuing.
Laser Weapon Armory:
    This is where the hero gets a neutron bomb to blow up the ship before getting to the escape pod. It has a keypad the hero has to guess the number for.
The Bridge:
    Another battle scene with a Gothon where the hero places the bomb.
Escape Pod:
    Where the hero escapes but only after guessing the right escape pod.
"""
#################### (Key Concepts)
#Nouns
"""
Alien
Player
Ship
Maze
Room
Scene
Gothon
Escape Pod
Planet
Map
Engine
Death
Central Corridor
Laser Weapon Armory
The Bridge
"""
#Verbs
"""
...
"""
####################
#CLASS HIERARCHY
"""
*Map
    -next_scene
    -opening_scene
*Engine
    -play
*Scene
    -enter
    *Death
    *Central Corridor
    *Laser Weapon Armory
    *The Bridge
    *Escape Pod
"""


