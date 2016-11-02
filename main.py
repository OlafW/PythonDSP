#!/usr/bin/env python3

import math
import numpy as np
import matplotlib.pyplot as plt

import util
import dft

# Multiplying two spectra as a form of filtering (convolution in time domain)
# x1 = uniform noise
# x2 = 1.0 / f^B (lowpass filter)

N = 512
B = 3.0
x1 = np.random.uniform(-1.0, 1.0, N)
R = np.empty(int(N/2))

# DFT of x1
X = dft.DFT(x1)

for n in range(int(N/2)):
    # Power spectrum
    re = X[n].real
    im = X[n].imag
    R[n] = re * re + im * im

    # Multiply X by x2 (1.0 / f^B)
    x2 = math.pow(n+1, B)
    R[n] /= x2

    # Reconstruct spectrum
    r = math.sqrt(R[n])
    phi = math.atan2(im, re)
    X[n] = r * (math.cos(phi) + math.sin(phi)*1j)
    X[N-1-n] = np.conjugate(X[n])

# IDFT of X
Y = dft.IDFT(X)

# Normalise real part of Y
y = np.empty(N)
for n in range(N):
    y[n] = Y[n].real

y = util.normalise(y)
R = util.normalise(R)

# Matplotlib
plt.loglog(R, basex=10, basey=10)
plt.xlim(0, R.size)
plt.ylim(-1.0, 1.0)
plt.show()
