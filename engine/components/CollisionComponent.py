
from typing import Callable
from pygame import Rect
import pygame
from engine.components.EntityComponent import EntityComponent
from engine.enums import CollisionResponse, CollisionMask, Mobility

class CollisionComponent(EntityComponent):
    def __init__(self):
        super().__init__()
        self._response : CollisionResponse = CollisionResponse.IGNORE
        self._active_overlaps : list['CollisionComponent'] = []
        self._cached_overlaps : list['CollisionComponent'] = []
        self._begin_overlap_calls : list[Callable[['CollisionComponent', 'CollisionComponent'], None]] = []
        self._end_overlap_calls : list[Callable[['CollisionComponent', 'CollisionComponent'], None]] = []
        self._hit_calls : list[Callable[['CollisionComponent', 'CollisionComponent'], None]] = []
        self._collision_mask : list[CollisionMask] = []
        self._collision_type : CollisionMask = CollisionMask.NONE
        self._mobility : Mobility = Mobility.STATIC
        self._x = 0
        self._y = 0
        self._width = 0
        self._height = 0

    def set_collision_type(self, collision_type: CollisionMask) -> None:
        self._collision_type = collision_type

    def set_offset(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def set_size(self, width: int, height: int) -> None:
        self._width = width
        self._height = height

    def add_to_collision_mask(self, collision_type: CollisionMask) -> None:
        self._collision_mask.append(collision_type)

    def remove_from_collision_mask(self, collision_type: CollisionMask) -> None:
        self._collision_mask.remove(collision_type)

    def bind_on_begin_ovelap(self, call: Callable[['CollisionComponent', 'CollisionComponent'], None]) -> None:
        self._begin_overlap_calls.append(call)

    def unbind_on_begin_ovelap(self, call: Callable[['CollisionComponent', 'CollisionComponent'], None]) -> None:
        self._begin_overlap_calls.remove(call)

    def bind_on_end_ovelap(self, call: Callable[['CollisionComponent', 'CollisionComponent'], None]) -> None:
        self._end_overlap_calls.append(call)

    def unbind_on_end_ovelap(self, call: Callable[['CollisionComponent', 'CollisionComponent'], None]) -> None:
        self._end_overlap_calls.remove(call)
    
    def bind_on_hit(self, call: Callable[['CollisionComponent', 'CollisionComponent'], None]) -> None:
        self._hit_calls.append(call)

    def unbind_on_hit(self, call: Callable[['CollisionComponent', 'CollisionComponent'], None]) -> None:
        self._hit_calls.remove(call)

    def set_response(self, response: CollisionResponse) -> None:
        self._response = response

    def get_response(self) -> CollisionResponse:
        return self._response
    
    def get_mobility(self) -> Mobility:
        return self._mobility
    
    def set_mobility(self, mobility: Mobility) -> None:
        self._mobility = mobility
    
    def can_collide_with(self, other: 'CollisionComponent') -> bool:
        return other._collision_type in self._collision_mask

    def on_collision(self, other: 'CollisionComponent') -> None:
        self._active_overlaps.append(other)

    def get_collision_bounds(self) -> Rect:
        return Rect(self._x + self._owner.x, self._y + self._owner.y, self._width, self._height)

    def hit(self, other: 'CollisionComponent') -> None:
        for call in self._hit_calls:
            call(self, other)

    def get_width(self) -> int:
        return self._width
    
    def get_height(self) -> int:
        return self._height
    
    def get_absolute_x(self) -> int:
        return self._x + self._owner.x
    
    def get_absolute_y(self) -> int:
        return self._y + self._owner.y

    def update_collisions(self) -> None:
        for overlap in self._active_overlaps:
            if overlap in self._cached_overlaps:
                self._cached_overlaps.remove(overlap)
            else:
                for call in self._begin_overlap_calls:
                    call(self, overlap)

        for overlap in self._cached_overlaps:
            for call in self._end_overlap_calls:
                call(self, overlap)

        # self._cached_overlaps.clear()
        self._cached_overlaps = self._active_overlaps
        self._active_overlaps = []


    # def draw(self, screen):
    #     pygame.draw.rect(screen, (255, 0, 0), self.get_collision_bounds(), 1)





