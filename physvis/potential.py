import numpy as np


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

    pos = int(pos*x.shape[0])
    width = int(width*x.shape[0])

    start = int(pos-width/2)
    end = int(pos+width/2)

    V[start:end, :] = height
    return V
