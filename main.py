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

    # wf = qmvis.wavefunction.wavepacket((0.5, 0), (-0.5, 0), 1.0, x)
    wf = qmvis.wavefunction.delta((0, 0), x)
    print('wf', wf.sum()*dxs[0]*dxs[1])

    V = qmvis.potential.double_slit(x)
    # V = qmvis.potential.barrier(0.75, 0.1, 200, x)

    particle_system = qmvis.ParticleSystem(
        [qmvis.QuantumParticle(x, wf)],
    )
    particle_system.particles[0].V = V

    @window.event
    def on_draw():
        window.clear()
        pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
        pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
        particle_system.draw(canvas)

    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == pyglet.window.key.X:
            particle_system.particles[0].measure_x()

    qmvis.clock.schedule_interval(lambda _: particle_system.update(dt), dt)

    qmvis.app.run()


if __name__ == '__main__':
    main()
