import numpy as np

from . import space


def delta(x_0, x):
    x_0 = np.asanyarray(x_0)
    inds = np.unravel_index(((x_0 - x)**2).sum(axis=-1).argmin(), x.shape[:-1])

    wf = np.zeros(x.shape[:-1])
    L = x[-1, -1] - x[0, 0]
    wf[inds] = L.prod()
    print(wf.sum())
    return wf



def wavepacket(k_0, x_0, a, x):
    k_0 = np.asanyarray(k_0)
    x_0 = np.asanyarray(x_0)

    x_0 = x_0/2*(x[-1, -1] - x[0, 0])
    k = space.k_from_x(x)
    k_0 = k_0/2*(k[-1, -1] - k[0, 0])

    norm = 1/(a*np.sqrt(np.pi))
    wf = (
        norm
        *np.exp(-0.5*(((x - x_0)/a)**2).sum(axis=-1))
        *np.exp(1j*(k_0*x).sum(axis=-1))
        #*np.exp(1j*(k_0*(x - x_0)).sum(axis=-1))
    )
    return wf
