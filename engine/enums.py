from enum import Enum


class CollisionResponse(Enum):
    IGNORE = 0
    OVERLAP = 1
    BLOCK = 2