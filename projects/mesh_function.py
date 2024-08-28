import numpy as np


def mesh_function(f, t):
    ft= np.zeros_like(t, dtype=float)
    for i in range(len(t)):
        ft[i]= f(t[i])
    return ft

def func(t):
    if 0 <= t <= 3:
        return np.exp(-t)
    else:
        return np.exp(-3*t)

def test_mesh_function():
    t = np.array([1, 2, 3, 4])
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-12)])
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)
