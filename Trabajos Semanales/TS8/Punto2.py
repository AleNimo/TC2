# -*- coding: utf-8 -*-

import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
import control

fs = 100e3
fc = 1e3

K = 2*fs

w0 = 2*np.pi*fc

numz_calc = [w0**2,2*w0**2,w0**2]
denz_calc = [K**2+np.sqrt(2)*K*w0+w0**2, 2*w0**2-2*K**2, K**2+w0**2-np.sqrt(2)*K*w0]

wz_calc, hz_calc = sig.freqz(numz_calc,denz_calc)

num, den = sig.butter(2, w0, btype='low', analog=True, output='ba')

ws, hs = sig.freqs(num,den)

numz, denz = sig.bilinear(num, den, fs)

wz, hz = sig.freqz(numz, denz)

fig, ax = plt.subplots(2,1,figsize=(10, 10))
ax[0].set_title('Comparación Filtro Analógico y digital')
ax[0].semilogx(ws, 20 * np.log10(abs(hs)), 'g', label=r'$|H(j \omega)|$')
ax[0].semilogx(wz_calc*fs, 20 * np.log10(abs(hz_calc)), 'r', label = r'$|H_z(e^{j \omega})|$ Calculado')
ax[0].semilogx(wz*fs, 20 * np.log10(abs(hz)), 'b--', label = r'$|H_z(e^{j \omega})|$ Scipy')
ax[0].set_ylabel('Amplitude [dB]')
ax[0].set_xlabel('Frequency [rad/sample]')
ax[0].legend()
ax[0].grid()

tf = control.pzmap(control.TransferFunction(numz,denz))
z,p,k = sig.tf2zpk([1,1,1], [1,0,0])
ax[0].show()