import numpy as np
import pyglet

import physvis


def main():
    canvas = physvis.Canvas()

    N = 100
    dx = 0.1
    x0 = -0.5*N*dx*np.asanyarray([1, 1])
    x = x0 + physvis.space.isotropic(N, dx)

    wf = physvis.wavefunction.wavepacket(
        (20, 0),
        (-2, 0),
        2.0,
        x,
    )
    V = np.zeros((N, N))
    V[70:80, :] = 1000000
    V[70:80, 40:45] = 0
    V[70:80, 55:60] = 0
    assert (x.shape[:-1] == wf.shape)

    particle_system = physvis.ParticleSystem([
        physvis.QuantumParticle(x, wf)
    ])
    particle_system.particles[0].V = V

    window = pyglet.window.Window()

    @window.event
    def on_draw():
        window.clear()
        particle_system.draw(canvas)

    pyglet.clock.schedule_interval(particle_system.update, 0.1)

    pyglet.app.run()


if __name__ == '__main__':
    main()
