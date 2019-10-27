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

    wf = qmvis.wavefunction.wavepacket((25, 0), (-2.5, 0), 1.0, x)
    # wf = qmvis.wavefunction.delta((0, 0), x)

    V = qmvis.potential.double_slit(x)
    # V = qmvis.potential.barrier(0.75, 0.1, 200, x)
    # V = qmvis.potential.inv_sq((0, 0), -0.0001, x)

    quantum_system = qmvis.QuantumSystem(
        [qmvis.QuantumParticle(x, wf)],
        V,
    )

    @window.event
    def on_draw():
        window.clear()
        pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
        pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
        quantum_system.draw(canvas)

    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == pyglet.window.key.X:
            quantum_system.particles[0].measure_x()

    def update(_):
        quantum_system.update(dt)

    qmvis.clock.schedule_interval(update, dt)

    qmvis.app.run()


if __name__ == '__main__':
    main()
