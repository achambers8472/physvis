import numpy as np

from . import space


# def delta(x_0, x):
#     x_0 = np.asanyarray(x_0)
#     inds = np.unravel_index(((x_0 - x)**2).sum(axis=-1).argmin(), x.shape[:-1])

#     wf = np.zeros(x.shape[:-1])
#     wf[inds] = 1
#     dx = x[1, 1] - x[0, 0]
#     wf = wf/((np.abs(wf)**2).sum()*dx.prod())
#     return wf

def delta(x_0, x):
    dx = x[1, 1] - x[0, 0]
    return wavepacket((0, 0), x_0, dx[0], x)


def wavepacket(k_0, x_0, a, x):
    k_0 = np.asanyarray(k_0)
    x_0 = np.asanyarray(x_0)

    k = space.k_from_x(x)

    norm = 1/(a*np.sqrt(np.pi))
    wf = (
        norm
        *np.exp(-0.5*(((x - x_0)/a)**2).sum(axis=-1))
        *np.exp(1j*(k_0*x).sum(axis=-1))
        #*np.exp(1j*(k_0*(x - x_0)).sum(axis=-1))
    )
    return wf
