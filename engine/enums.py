from enum import Enum


class CollisionResponse(Enum):
    IGNORE = 0
    OVERLAP = 1
    BLOCK = 2


class CollisionMask(Enum):
    NONE = 0
    MASK1 = 1
    MASK2 = 2
    MASK3 = 3
    MASK4 = 4
    MASK5 = 5