import numpy as np
import matplotlib.pyplot as plt
import util

# f0 estimation with cepstrum.
# Plot of cepstrum of test signal shows a peak at the fundamental, 440Hz (and DC...)

fs = 44100.0
N = 1024
f0 = 440.0
H = 10
harmonics = np.arange(1, H+1)
phi = np.random.random(H) * np.pi

# Test signal
x = np.zeros(N)

for n in range(N):
    for h in harmonics:
        x[n] += np.cos(2.0 * np.pi * n / fs * h * f0) / h

x = util.normalise(x)

# Compute magnitude spectrum
X = np.fft.rfft(x)
M = abs(X)

# Fourier transform of log(magnitude spectrum)
C = np.fft.rfft(np.log2(M))
Mc = abs(C)
Mc = util.normalise(Mc)

# Find highest bin (ignore first 10 bins)
DC = 10
maxbin = np.argmax(Mc[DC:]) + DC
f0_estimate = (fs / 2.0) / maxbin

print('f0 estimation: {}Hz' .format(f0_estimate))

# Plot magnitude spectrum of cepstrum
plt.xscale('log', basex=2)
plt.xlabel('bin')
plt.ylabel('amplitude')
plt.plot(Mc[DC:])
plt.show()
