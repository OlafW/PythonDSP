#!/usr/bin/env python3

import cmath
import numpy as np
import matplotlib.pyplot as plt

'''
    Analysing n-order LTI FIR systems
    Simple 1st order example: y[n] = 0.5x[n] + 0.5x[n-1]
'''


def analyseFIR(N, numOrder, coeff):
    H = np.zeros(N, dtype=complex)

    for n in range(N):
        f = n * cmath.pi / (N-1)
        for k in range(numOrder):
            z = cmath.exp(-1.0j * f * k)
            H[n] += coeff[k] * z

    return H


if __name__ == "__main__":
    N = 100                         # number of frequencies to calculate
    coeff = np.array([0.5, 0.5])    # 2 coefficients (1st order filter)
    numOrder = coeff.size

    H = analyseFIR(N, numOrder, coeff) # analysis result
    A = np.empty(N)                    # amplitude spectrum
    PHI = np.empty(N)                  # phase spectrum

    for n in range(N):
        A[n] = abs(H[n])
        PHI[n] = cmath.phase(H[n])

    # plot amplitude spectrum
    plt.xlim(0, N)
    plt.ylim(0.0, 1.0)
    plt.plot(A)
    plt.show()
