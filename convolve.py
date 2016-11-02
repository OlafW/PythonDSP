#!/usr/bin/env python3

import math
import numpy as np
import matplotlib.pyplot as plt
import util
import dft

def convolve(x1, x2):
    N = x1.size
    M = x2.size
    y = np.zeros(N+M-1)

    for n in range(N):
        for m in range(M):
            y[n+m] += x1[n] * x2[m]

    return util.normalise(y)


def autoCorrelate(x):
    N = x.size
    y = np.zeros(N)

    for n in range(1, N):
        sum = 0.0
        for m in range(N - n):
            sum += x[m] * x[m + n]

        y[n] = abs(sum) / (N - n)

    return y


def YIN(x):
    N = x.size
    y = np.zeros(N)

    for n in range(1, N):
        diff = 0.0
        for m in range(N - n):
            diff += pow(x[m] - x[m + n], 2)

        y[n] = diff

    return y


if __name__ == "__main__":
    fn = "/Users/olafwisselink/Code/sms-tools/sounds/flute-A4.wav"
    fs, x = util.readwav(fn)
    N = x.size

    # Magnitude spectrum of x
    X = np.fft.rfft(x, norm="ortho")
    M = abs(X)
    M = util.normalise(M)

    # Matplotlib
    plt.loglog(M, basex=10, basey=10)
    plt.xlim(0, X.size)
    plt.ylim(0, 1)
    plt.show()
