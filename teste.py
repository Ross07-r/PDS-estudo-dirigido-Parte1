import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 100)

# sinal composto
x = np.sin(0.1*np.pi*n) + np.sin(0.4*np.pi*n)

X = np.fft.fft(x)
freq = np.fft.fftfreq(len(x))

plt.plot(freq, np.abs(X))
plt.title("DFT - Múltiplas Frequências")
plt.grid()
plt.show()
