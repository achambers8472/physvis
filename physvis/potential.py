import numpy as np


def constant(a, x):
    return a*np.ones(x.shape[:-1])


def double_slit(x):
    V = np.zeros(x.shape[:-1])
    V[74:75, :] = 1000000
    V[74:75, 40:45] = 0
    V[74:75, 55:60] = 0
    V[-1, :] = 1000000
    return V


def barrier(pos, width, height, x):
    pos = np.asanyarray(pos)
    V = np.zeros(x.shape[:-1])

    inds = (x[:, :, 0] > (pos - width/2)) & (x[:, :, 0] < (pos + width/2))

    V[inds] = height
    return V


def inv_sq(x_0, a, x):
    V = a/((x - x_0)**2).sum(axis=-1)
    V[np.isnan(V)] = 0
    return V


def well(radius, width, height, x):
    V = np.zeros(x.shape[:-1])
    r = (x**2).sum(axis=-1)
    inds = (radius < r) & (r < radius + width)
    V[inds] = height
    return V
