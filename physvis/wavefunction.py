import numpy as np


def wavepacket(x_0, a, x):
    Dx = x_0 - x
    print(Dx.shape)
    wf = np.exp(-(Dx**2).sum(axis=-1)/(2*a))
    return wf
