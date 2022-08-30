# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 22:51:15 2022

@author: Alejo
"""

import numpy as np
import scipy.signal as sig
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys

# Setup inline graphics
mpl.rcParams['figure.figsize'] = (10,10)

#%% Datos y Plantilla

fs = 1000

#Plantilla
fpass = np.array( [3, 25] )
ripple = 5 # dB
fstop = np.array( [1, 35] )
attenuation = 45 # dB

#%%Creación de filtro IIR
#Obtengo orden y frecuencias donde la atenuación es 3dB
order_IIR, wcutofz = sig.buttord( fpass, fstop, ripple, attenuation, analog=False, fs=fs)

#Obtengo coeficientes del filtro IIR
SOS = sig.iirfilter(order_IIR, wcutofz, rp=None, rs=attenuation, btype='bandpass', analog=False, ftype='butter', output='sos', fs=fs)

wz_target = np.linspace(0.00001,100,400)
wz_IIR, H_IIR = sig.sosfreqz(SOS,wz_target,fs=fs)

ganancia = 1.77827941

#%%Creación de filtro FIR
order_FIR = 2001
bands = [0,1,3,25,27,fs/2]
desired = [0,0,1,1,0,0]
coeff = sig.firls(order_FIR, bands, desired, weight=None, nyq=None, fs=fs)

wz_FIR, H_FIR = sig.freqz(coeff,1,wz_target,fs=fs)


#%%Ploteo
plt.plot(wz_IIR, 20*np.log10(np.abs(H_IIR*ganancia)), label = 'IIR_Butter_orden_%d' %order_IIR)
plt.plot(wz_FIR, 20*np.log10(np.abs(H_FIR)), label = 'FIR_Least-Squares_orden_%d' %order_FIR)
plt.title('Plantilla de diseño')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud [dB]')
plt.grid(which='both', axis='both')
plt.xlim([0,100])
plt.ylim([-60,10])
plt.legend()

#ploteo plantilla
plt.fill([0, 1, 1,35,35,100,100,25,25,3,3,0],[-40,-40,5,5,-40,-40,-60,-60,0,0,-60,-60],color=[0.8,0.902,0.8])
plt.plot(1,-40,3,0,25,0,35,-40, marker='x', color = 'k')

