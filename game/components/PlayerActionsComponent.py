from engine import EntityComponent, CollisionComponent
from engine import Engine
import pygame

class PlayerActionsComponent(EntityComponent):
    def __init__(self):
        super().__init__()
        self._acc = 0
        self._acc_value = 800
        self._vel = 0
        self._max_vel = 900
        self._move_l = False
        self._move_r = False
        self._is_moving = False

    def update(self, dt):
        super().update(dt)
        events = Engine.get().get_events()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._move_l = True
                if event.key == pygame.K_RIGHT:
                    self._move_r = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self._move_l = False
                if event.key == pygame.K_RIGHT:
                    self._move_r = False
        self.move(dt)

    def move(self, dt):
        if self._move_l == self._move_r:
            if self._is_moving:
                self._acc = - self._acc
                self._is_moving = False
            else:
                if self._vel == 0:
                    self._acc = 0
        elif self._move_l:
            self._is_moving = True
            self._acc = -self._acc_value
        elif self._move_r:
            self._is_moving = True
            self._acc = self._acc_value

        if self._vel * (self._vel + self._acc) < 0:
            self._vel = 0
        else:
            self._vel = dt * self._acc + self._vel if abs(self._vel + self._acc * dt) <= self._max_vel else self._max_vel * (self._acc / abs(self._acc))

        self._owner.x += self._vel * dt


    def on_overlap(self, component: CollisionComponent, other : CollisionComponent):
        print("MAM CIE")

        

    
        