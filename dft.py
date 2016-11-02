#!/usr/bin/env python3

import cmath
import numpy as np
import util

# Discrete Fourier Transform

def DFT(x):
    N = x.size
    half_N = int(N / 2)
    X = np.zeros(N, dtype=complex)

    for k in range(N):
        for n in range(N):
            X[k] += x[n] * cmath.exp(util.TWOPI * -1.0j / N * n * k)
        X[k] /= N

    return X


def IDFT(X):
    N = X.size
    x = np.zeros(N, dtype=complex)

    for n in range(N):
        for k in range(N):
            x[n] += X[k] * cmath.exp(util.TWOPI * 1.0j / N * n * k)

    return x
