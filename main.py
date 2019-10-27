import physvis


def main(window_size=(1280, 640)):
    N_x = [100, 100]
    dxs = [0.1, 0.1]
    x = physvis.space.normal(N_x, dxs)
    dt = 0.01

    particle = physvis.QuantumParticle.wavepacket((25, 0), (-2.5, 0), 1.0, x)
    # particle = physvis.QuantumParticle.delta((0, 0), x)

    V = physvis.potential.double_slit(x)
    # V = physvis.potential.barrier(0.75, 0.1, 200, x)
    # V = physvis.potential.inv_sq((0, 0), -0.0001, x)

    quantum_system = physvis.QuantumSystem([particle], V)
    simulation = physvis.Simulation(quantum_system, dt)

    simulation.run()


if __name__ == '__main__':
    main()
