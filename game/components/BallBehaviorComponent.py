from engine import EntityComponent, Engine
from engine import CollisionComponent
from game.GameManager import GameManager

class BallBehaviorComponent(EntityComponent):
    def __init__(self):
        super().__init__()
        self._vel = [0, 0]
        self._window = None
        self._starting = True
        self._acc = 330
        self._width = 0
        self._refraction_strength = 0.7
        self._already_hit = False
        self._slowdown = 0.2
        self._num_slowdowns = 0
        self._bounce_margin = 5

    def set_width(self, width):
        self._width = width

    def load(self):
        super().load()
        self._max_vel_mult = GameManager.get().get_ball_vel()
        self._vel_mult = GameManager.get().get_ball_vel() // 100
        self._vel = [1, -1]
        self._window = Engine.get().get_window_size()
        self._starting = True


    def update(self, dt):
        super().update(dt)
        if self._starting:
            if self._vel_mult < self._max_vel_mult:
                self._vel_mult += self._acc * dt
                self.diagonal_correction()
            else:
                self._vel_mult = self._max_vel_mult
                self._starting = False

        self._owner.x += self._vel[0] * dt
        self._owner.y += self._vel[1] * dt

        if self._owner.x < 0 or self._owner.x + self._width > self._window[0]:
            self._vel[0] = -self._vel[0]
        if self._owner.y < 0: 
            self._vel[1] = -self._vel[1]
        elif self._owner.y > self._window[1]:
            Engine.get().get_active_scene().remove_entity(self._owner)
            GameManager.get().on_lost()
  
    def on_overlap(self, component: CollisionComponent, other : CollisionComponent):
        if other._owner.get_name() == "platform":
            self.bounce_from_platform(component, other)
        if other._owner.get_name() == "brick":
            self.bounce_from_brick(component, other)

    def bounce_from_platform(self, component : CollisionComponent, other : CollisionComponent):
        middle = other._owner.x + other.get_width() // 2
        half_width = other.get_width() // 2
        mid_dist = component._owner.x + component.get_width() // 2 - middle
        refraction_factor = mid_dist / half_width
        vel_change = refraction_factor * self._refraction_strength * self._vel_mult
        self._vel[0] += vel_change
        self._vel[1] = -self._vel[1]
        self.diagonal_correction()

    def diagonal_correction(self):
        vel_diagonal = (self._vel[0] ** 2 + self._vel[1] ** 2) ** 0.5
        x_mult = self._vel[0] / vel_diagonal
        y_mult = self._vel[1] / vel_diagonal
        self._vel[0] = x_mult * self._vel_mult
        self._vel[1] = y_mult * self._vel_mult

    def bounce_from_brick(self, component : CollisionComponent, other : CollisionComponent):
        if other._owner.get_component("BrickBehaviorComponent").does_change_ball_speed():
            self.slow_down()
        if abs(component.get_absolute_x() + component.get_width() - other.get_absolute_x()) < self._bounce_margin:
            self._vel[0] = -abs(self._vel[0])    
        elif abs(other.get_absolute_x() + other.get_width() - component.get_absolute_x()) < self._bounce_margin:
                self._vel[0] = abs(self._vel[0])
        if abs(component.get_absolute_y() + component.get_height() - other.get_absolute_y()) < self._bounce_margin:
                self._vel[1] = -abs(self._vel[1])
        elif abs(other.get_absolute_y() + other.get_height() - component.get_absolute_y()) < self._bounce_margin:
                self._vel[1] = abs(self._vel[1])
           
    def slow_down(self):
        self._starting = False
        self._num_slowdowns += 1
        self._vel_mult *= (1 - self._slowdown)
        self.diagonal_correction()
        Engine.get().set_function_delay(self.reset, 5)


    def reset(self):
        self._num_slowdowns -= 1
        if self._num_slowdowns == 0:
            self._starting = True