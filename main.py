import functools

import numpy as np
import pyglet

import physvis


def main():
    canvas = physvis.Canvas()

    Ns = [100, 100]
    dxs = [0.1, 0.1]
    x = physvis.space.normal(Ns, dxs)
    dt = 0.01

    wf = physvis.wavefunction.wavepacket(
        (20, 0),
        (-3, 0),
        1.0,
        x,
    )
    V = np.zeros(Ns)

    V[74:75, :] = 1000000
    V[74:75, 40:45] = 0
    V[74:75, 55:60] = 0
    V[-1, :] = 1000000

    # V[65:75, :] = 160

    assert (x.shape[:-1] == wf.shape)

    particle_system = physvis.ParticleSystem(
        [physvis.QuantumParticle(x, wf)],
    )
    particle_system.particles[0].V = V

    window = pyglet.window.Window()
    window.config.alpha_size = 8

    @window.event
    def on_draw():
        window.clear()
        pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
        pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
        particle_system.draw(canvas)

    pyglet.clock.schedule_interval(lambda _: particle_system.update(dt), dt)

    pyglet.app.run()


if __name__ == '__main__':
    main()
