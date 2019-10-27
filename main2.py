import functools

import pyglet

import physvis as qmvis


def main(window_size=(1280, 640)):
    window = qmvis.Window(window_size)
    canvas = qmvis.Canvas(window_size)

    N_x = [100, 100]
    dxs = [0.1, 0.1]
    x = qmvis.space.normal(N_x, dxs)
    dt = 0.01

    classical_system = qmvis.ClassicalSystem(
        [qmvis.ClassicalParticle(x, (0, 0), (1, 0))],
        [qmvis.force.uniform_gravity],
    )

    @window.event
    def on_draw():
        window.clear()
        pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
        pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
        classical_system.draw(canvas)

    def update(_):
        classical_system.update(dt)

    qmvis.clock.schedule_interval(update, dt)

    qmvis.app.run()


if __name__ == '__main__':
    main()
