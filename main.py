import functools

import numpy as np
import pyglet

import physvis


def main():
    canvas = physvis.Canvas()

    N = 100
    dx = 0.1
    x0 = -0.5*N*dx*np.asanyarray([1, 1])
    x = x0 + physvis.space.isotropic(N, dx)
    dt = 0.001

    wf = physvis.wavefunction.wavepacket(
        (20, 0),
        (-2, 0),
        2.0,
        x,
    )
    V = np.zeros((N, N))
    V[74:75, :] = 1000000
    V[74:75, 40:45] = 0
    V[74:75, 55:60] = 0
    V[-1, :] = 1000000
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

    pyglet.clock.schedule(lambda _: particle_system.update(dt))

    pyglet.app.run()


if __name__ == '__main__':
    main()
