import numpy as np


def wavepacket(p_0, x_0, a, x):
    p_0 = np.asanyarray(p_0)
    x_0 = np.asanyarray(x_0)
    norm = 1/(a*np.pi**0.5)
    wf = (
        norm
        *np.exp(-0.5*(((x - x_0)/a)**2).sum(axis=-1))
        *np.exp(1j*(p_0*(x - x_0)).sum(axis=-1))
    )
    return wf
