import pyglet


class Window:
    def __init__(self, size):
        self._window = pyglet.window.Window(width=1080, height=1080)
        self._window.config.alpha_size = 8

    def event(self, callback):
        return self._window.event(callback)

    def clear(self, *args, **kwargs):
        self._window.clear()
