import numpy as np
import pyglet

import physvis


def cartesian_product(*arrays):
    la = len(arrays)
    dtype = np.result_type(*arrays)
    arr = np.empty([len(a) for a in arrays] + [la], dtype=dtype)
    for i, a in enumerate(np.ix_(*arrays)):
        arr[...,i] = a
    return arr.reshape(-1, la)


def main():
    canvas = physvis.Canvas()

    x = physvis.space.isotropic(500)
    wf = physvis.wavefunction.wavepacket(
        (10, 20),
        (250, 250),
        50,
        x,
    )
    V = np.zeros((500, 500))
    V[400:410, :] = 1000
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

    pyglet.clock.schedule_interval(particle_system.update, 0.01)

    pyglet.app.run()


if __name__ == '__main__':
    main()
