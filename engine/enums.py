from enum import Enum


class CollisionResponse(Enum):
    IGNORE = 0
    OVERLAP = 1

class Mobility(Enum):
    STATIC = 0
    DYNAMIC = 1

class CollisionMask(Enum):
    NONE = 0
    MASK1 = 1
    MASK2 = 2
    MASK3 = 3
    MASK4 = 4
    MASK5 = 5