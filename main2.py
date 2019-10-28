import physvis


def main(window_size=(1280, 640)):
    N_x = [100, 100]
    dxs = [0.1, 0.1]
    x = physvis.space.normal(N_x, dxs)
    dt = 0.01

    system = physvis.ClassicalSystem(
        [
            physvis.ClassicalParticle(x, (0, 0), (1, 0)),
            physvis.ClassicalParticle(x, (0.5, 0), (1, -1)),
        ],
        # [physvis.force.uniform_gravity],
        [physvis.force.gravity],
    )

    simulation = physvis.Simulation(system, dt)

    simulation.run()


if __name__ == '__main__':
    main()
