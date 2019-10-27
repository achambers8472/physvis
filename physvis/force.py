import numpy as np


def uniform_gravity(particles, g=-9.8):
    F = np.zeros((len(particles), 2))
    F[:, 1] = g
    return F
