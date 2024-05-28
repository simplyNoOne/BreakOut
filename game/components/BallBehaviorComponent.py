from engine import EntityComponent, Engine
from engine import CollisionComponent
from game.GameManager import GameManager

class BallBehaviorComponent(EntityComponent):
    def __init__(self):
        super().__init__()
        self._vel = [0, 0]
        self._window = None

    def load(self):
        super().load()
        vel = GameManager.get().get_ball_vel()
        self._vel = [vel, vel]
        self._window = Engine.get().get_window_size()


    def update(self, dt):
        super().update(dt)
        self._owner.x += self._vel[0] * dt
        self._owner.y += self._vel[1] * dt

        if self._owner.x < 0 or self._owner.x > self._window[0]:
            self._vel[0] = -self._vel[0]
        if self._owner.y < 0: 
            self._vel[1] = -self._vel[1]
        elif self._owner.y > self._window[1]:
            GameManager.get().on_lost()
  
    def on_overlap(self, component: CollisionComponent, other : CollisionComponent):
        print(other._owner.get_name())
        if other._owner.get_name() == "platform":
            self._vel[1] = -self._vel[1]
        


