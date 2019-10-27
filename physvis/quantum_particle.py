import numpy as np

from . import space
from . import wavefunction


def normsq(psi):
    return np.abs(psi)**2


class QuantumParticle:
    def __init__(self, x, psi_x, m=1):
        self.x = x
        self.psi_x = psi_x
        self.m = m

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x
        self._dxs = self.x[1, 1] - self.x[0, 0]
        x0 = self._x[0, 0]

        Ns = self.x.shape[:-1]

        self._dks = (2*np.pi)/(Ns*self._dxs)
        self._k = space.normal(Ns, self._dks)
        k0 = self._k[0, 0]

        _k0_dot_x = (k0*self.x).sum(axis=-1)
        _x0_dot_k = (x0*self.k).sum(axis=-1)

        self._x_mod_factor = np.exp(-1j*_k0_dot_x)*self._dxs.prod()/(2*np.pi)
        self._x_unmod_factor = np.exp(1j*_k0_dot_x)*(2*np.pi)/self._dxs.prod()

        self._k_unmod_factor = np.exp(-1j*_x0_dot_k)
        self._k_mod_factor = np.exp(-1j*_x0_dot_k)

        self._k2 = (self._k**2).sum(axis=-1)

    @property
    def k(self):
        return self._k

    @k.setter
    def k(self, k):
        raise NotImplementedError()

    @property
    def psi_x(self):
        return self._psi_mod_x*self._x_unmod_factor

    @psi_x.setter
    def psi_x(self, psi_x):
        self._psi_mod_x = self._x_mod_factor*psi_x
        self._psi_mod_k = self._mod_x_to_mod_k(self._psi_mod_x)

    @property
    def psi_k(self):
        return self._psi_mod_k*self._k_unmod_factor

    @psi_k.setter
    def psi_k(self, psi_k):
        raise NotImplementedError()
        self._psi_mod_k = self._k_mod_factor*psi_k

    def _mod_x_to_mod_k(self, psi_mod_x):
        return np.fft.fft2(psi_mod_x)

    def _mod_k_to_mod_x(self, psi_mod_k):
        return np.fft.ifft2(psi_mod_k)

    def update(self, V, dt):
        x_half_up_factor = np.exp((-0.5j*dt)*V)

        self._psi_mod_x *= x_half_up_factor

        self._psi_mod_k = self._mod_x_to_mod_k(self._psi_mod_x)
        self._psi_mod_k *= np.exp((-0.5j*dt/self.m)*self._k2)
        self._psi_mod_x = self._mod_k_to_mod_x(self._psi_mod_k)

        self._psi_mod_x *= x_half_up_factor

    def draw(self, canvas):
        p_x = self.prob_x
        p_k = self.prob_k
        canvas.draw_array((0, 0), p_x/0.001)
        canvas.draw_array((640, 0), p_k/0.001)

    @property
    def prob_x(self):
        tmp = normsq(self.psi_x)*self._dxs.prod()
        print(tmp.sum())
        return tmp


    @property
    def prob_k(self):
        tmp = normsq(self.psi_k)*self._dks.prod()
        print(tmp.sum())
        return tmp

    def measure_x(self):
        p_x = self.prob_x
        flat = p_x.flatten()
        flat = flat/flat.sum()
        print(flat.sum())
        ind = np.random.choice(np.arange(len(flat)), p=flat)
        print(ind)
        ind = np.unravel_index(ind, p_x.shape)
        print(ind)
        print(self.x.shape)
        x_0 = self.x[ind]
        print(x_0)
        self.psi_x = wavefunction.wavepacket((0, 0), x_0, self._dxs[0], self.x)
