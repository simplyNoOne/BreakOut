#BreakOut

# run on NoEngine # 

This is a simple Breakout-type game running on a simple custom engine - NoEngine - written using pygame. (yes, creating any semblence of a game engine using python is crazy, hence the atrocius performance)


A detour to the engine:

The engine itself is rather slow, but checks all basic criteria of what a game engine ought to be.

It loads resources at the beginning, allows you to define and populate scenes, tracks collisions and informs relevant collision components about the occurence of overlap. Allows for masks as well as static and dynamic entities.

Tips for using NoEngine:
 - Logic should be split between components that are added to relevant entities.
 - Scenes, entities and components are all loaded automatically provided that they are added in the designated spots. Entities must be added to the populate_scene function in your Scene, Components must be created in the add_components function in your Entity. 
 - You can define and reuse your own scenes, entities and components, and to do so, you must register them with the ResourceManager in the main game file.
 - Each frame you can query the Engine for the events.
 - You can customize Components' update functions as well as create you own drawing logic.
 - You can adjust the load and unload behaviour of the Scenes, Entities and Components.

Base components provided by the engine:
 - CollisionComponent - each Entity that is to collide must have it, the Entity must register its Component for collision manually with the Engine.
 - TextureComponent - allows for the Entity to be drawn on screen, can display both textures and texts.
 - SoundComponent - allows to play sound effects.


Back to the game:

You can run BreakOut automatically using run_BreakOut.bat for Windows or run_BreakOut.sh for Unix based system.

... Enjoy