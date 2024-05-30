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
        self._already_hit = False

    def set_width(self, width):
        self._width = width

    def load(self):
        super().load()
        vel = GameManager.get().get_ball_vel()
        self._vel = [1, -1]
        self._max_vel = [vel, vel]
        self._window = Engine.get().get_window_size()
        self._starting = True


    def update(self, dt):
        super().update(dt)
        self._already_hit = False
        if self._starting:
            if abs(self._vel[1]) < self._max_vel[1]:
                self._vel[1] += self._acc * dt * (self._vel[1] / abs(self._vel[1]))
                self._vel[0] += self._acc * dt * (self._vel[0] / abs(self._vel[0]))
            else:
                self._vel[1] = self._max_vel[1] * (self._vel[1] / abs(self._vel[1]))
                self._vel[0] = self._max_vel[0] * (self._vel[0] / abs(self._vel[0]))
                self._starting = False

        self._owner.x += self._vel[0] * dt
        self._owner.y += self._vel[1] * dt

        if self._owner.x < 0 or self._owner.x + self._width > self._window[0]:
            self._vel[0] = -self._vel[0]
        if self._owner.y < 0: 
            self._vel[1] = -self._vel[1]
        elif self._owner.y > self._window[1]:
            GameManager.get().on_lost()
  
    def on_overlap(self, component: CollisionComponent, other : CollisionComponent):
        if self._already_hit:
            return
        self._already_hit = True
        if other._owner.get_name() == "platform":
            self.calc_new_dir(component, other)
        if other._owner.get_name() == "brick":
            self.change_dir(component, other)

    def calc_new_dir(self, component : CollisionComponent, other : CollisionComponent):
        platform_hit_spot = component._owner.x + component.get_width() // 2 - other._owner.x
        if platform_hit_spot < other.get_width() // 3:
            self._vel[0] = self._vel[0] - self._vel[0] // 10
        elif platform_hit_spot > other.get_width() * 2 // 3:
            self._vel[0] = self._vel[0] + self._vel[0] // 10
        
        
        self._vel[1] = -self._vel[1]
            
            

    def change_dir(self, component : CollisionComponent, other : CollisionComponent):
        change_y = True
        if abs(component._owner.x + component.get_width() - other._owner.x) < 1:
            change_y = False
        elif abs(other._owner.x + other.get_width() - component._owner.x) < 1:
            change_y = False
        if change_y:
            self._vel[1] = -self._vel[1]
        else:
            self._vel[0] = -self._vel[0]
        



