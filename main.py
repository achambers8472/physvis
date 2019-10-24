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

    x = cartesian_product(np.arange(320), np.arange(320))
    wf = physvis.wavefunction.wavepacket((50, 50), 30, x)
    print(x.shape, wf.shape)
    assert (x.shape[:-1] == wf.shape)

    particle_system = physvis.ParticleSystem([
        physvis.QuantumParticle(x, wf)
    ])

    window = pyglet.window.Window()

    @window.event
    def on_draw():
        window.clear()
        particle_system.draw(canvas)

    pyglet.clock.schedule_interval(particle_system.update, 0.1)

    pyglet.app.run()


if __name__ == '__main__':
    main()
