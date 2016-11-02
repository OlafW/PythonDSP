#!/usr/bin/env python3

import math
import numpy as np
from scipy.io.wavfile import read, write

# Constants
TWOPI = 2.0 * math.pi

# File IO
def readwav(fn):
    fs, x = read(fn)
    return fs, x

def writewav(x, fs, fn):
    write(fn, fs, x)

def normalise(x):
    return x / float(np.max(np.abs(x)))
