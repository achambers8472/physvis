import numpy as np


def normal(Ns, dxs):
    axes = [-0.5*N*dx + np.arange(N)*dx for N, dx in zip(Ns, dxs)]
    return np.stack(np.meshgrid(*axes, indexing='ij'), axis=-1)
