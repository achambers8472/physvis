import pyglet

from . import app
from . import canvas
from . import clock
from . import space
from . import window


class Simulation:
    def __init__(self, system, dt, window_size=(1280, 640)):
        self.system = system
        self.dt = dt
        self.window = window.Window(window_size)
        self.canvas = canvas.Canvas(window_size)
        self._paused = False

        @self.window.event
        def on_draw():
            self.window.clear()
            pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
            pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
            self.system.draw(self.canvas)

        @self.window.event
        def on_key_press(symbol, modifiers):
            {
                # pyglet.window.key.X: self.system.particles[0].measure_x,
                pyglet.window.key.SPACE: self.toggle_pause,
            }.get(symbol, lambda: print(f"{symbol} is not bound!"))()

        def update(_):
            if not self._paused:
                self.system.update(dt)

        clock.schedule_interval(update, 1/60)

    def toggle_pause(self):
        self._paused = not self._paused

    def run(self):
        app.run()
