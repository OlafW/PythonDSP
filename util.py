#!/usr/bin/env python3

import math
import numpy as np
from scipy.io.wavfile import read, write

# Constants
TWOPI = 2.0 * math.pi

# File IO
def readwav(fn):
    fs, x = read(path)

    return fs, normalise(x)

def writewav(fn, x, fs = 44100.0):
    write(fn, x, fs)

def normalise(x):
    return x / float(np.max(np.abs(x)))


# Windowing functions
def hammingWindow(N):
    y = np.empty(N)
    a = 0.54

    for n in range(N):
        y[n] = a - (1.0 - a) * math.cos(TWOPI / N * n)

    return y

def triangularWindow(N):
    y = np.empty(N)
    L = (N-1) / 2.0

    for n in range(N):
        y[n] = 1.0 - abs( (n - L) / L  )

    return y

def rectangularWindow(N, w):
    y = np.empty(N)

    for n in range(N):
        y[n] = math.cos(TWOPI / N * n) < w

    return y
