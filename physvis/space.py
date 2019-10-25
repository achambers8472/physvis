import numpy as np


def normal(Ns, dxs):
    axes = [-0.5*N*dx + np.arange(N)*dx for N, dx in zip(Ns, dxs)]
    return np.stack(np.meshgrid(*axes, indexing='ij'), axis=-1)


def k_from_x(x):
    L_x = x[-1, -1] - x[0, 0]
    dks = (2*np.pi)/L_x
    k = normal(x.shape[:-1], dks)
    return k
