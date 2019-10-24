import numpy as np
import pyglet

import physvis


def main():
    canvas = physvis.Canvas()

    x = physvis.space.isotropic(500)
    wf = physvis.wavefunction.wavepacket(
        (2, 0),
        (250, 250),
        50,
        x,
    )
    V = np.zeros((500, 500))
    V[400:, :] = 1000000
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
