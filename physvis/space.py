import numpy as np


def isotropic(N, dx=1):
    tmp = np.arange(N)*dx
    return np.stack(np.meshgrid(tmp, tmp, indexing='ij'), axis=-1)
