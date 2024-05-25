from typing import Callable
from engine.components.EntityComponent import EntityComponent
from engine.enums import CollisionResponse

class CollisionComponent(EntityComponent):
    def __init__(self):
        super().__init__()
        self._response : CollisionResponse = CollisionResponse.IGNORE
        self._active_overlaps : list['CollisionComponent'] = []
        self._cached_overlaps : list['CollisionComponent'] = []
        self._begin_overlap_calls : list[Callable[['CollisionComponent', 'CollisionComponent'], None]] = []
        self._end_overlap_calls : list[Callable[['CollisionComponent', 'CollisionComponent'], None]] = []
        self._hit_calls : list[Callable[['CollisionComponent', 'CollisionComponent'], None]] = []
        self._collides_with : list['CollisionComponent'] = None

    def add_to_collides_with(self, other: 'CollisionComponent') -> None:
        self._collides_with.append(other)

    def remove_from_collides_with(self, other: 'CollisionComponent') -> None:
        self._collides_with.remove(other)

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

    def get_response(self) -> CollisionResponse:
        return self._response
    
    def collides_with(self, other: 'CollisionComponent') -> bool:
        return other in self._collides_with

    def on_collision(self, other: 'CollisionComponent') -> None:
        if self._response == CollisionResponse.BLOCK and other.get_response() == CollisionResponse.BLOCK:
            self.hit(other)
        else:
            self._active_overlaps.append(other)


    def hit(self, other: 'CollisionComponent') -> None:
        for call in self._hit_calls:
            call(self, other)


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

        self._cached_overlaps.clear()
        self._cached_overlaps = self._active_overlaps
        self._active_overlaps = []