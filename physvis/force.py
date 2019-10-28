import numpy as np


def uniform_gravity(particles, g=-9.8):
    F = np.zeros((len(particles), 2))
    F[:, 1] = g
    return F


def gravity(particles, G=1):
    Fs = []
    for p1 in particles:
        F = np.zeros((2,))
        for p2 in (p for p in particles if p is not p1):
            dx = p1.pos - p2.pos
            mod_dx = np.sqrt((dx**2).sum())
            F += -(G*p1.mass*p2.mass*dx)/(mod_dx**3)
        Fs.append(F)
    return Fs
