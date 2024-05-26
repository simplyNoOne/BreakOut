from engine import EntityComponent, Engine

class BallBehaviorComponent(EntityComponent):
    def __init__(self):
        super().__init__()
        self._vel = [600,800]
        self._window = None

    def load(self):
        self._window = Engine.get().get_window_size()

    def update(self, dt):
        super().update(dt)
        self._owner.x += self._vel[0] * dt
        self._owner.y += self._vel[1] * dt

        if self._owner.x < 0 or self._owner.x > self._window[0]:
            self._vel[0] = -self._vel[0]
        if self._owner.y < 0 or self._owner.y > self._window[1]:
            self._vel[1] = -self._vel[1]



