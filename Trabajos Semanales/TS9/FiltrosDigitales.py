# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 22:51:15 2022

@author: Alejo
"""

import numpy as np
import scipy.signal as sig
import matplotlib as mpl
import matplotlib.pyplot as plt


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

ganancia = 10**(5/20) #5dB

#%%Creación de filtro FIR
cant_coeff_FIR = 1501
bands = [0,1,3,25,27,fs/2]
desired = [0,0,1,1,0,0]
coeff_FIR = sig.firls(cant_coeff_FIR, bands, desired, weight=None, nyq=None, fs=fs)

wz_FIR, H_FIR = sig.freqz(coeff_FIR,1,wz_target,fs=fs)


#%%Respuesta de módulo, fase, y retardo de grupo

plt.close('all')
fig, ax = plt.subplots(4,1, figsize = (15,10))
ax[0].plot(wz_IIR, 20*np.log10(np.abs(H_IIR*ganancia)), label = 'IIR_Butter_orden_%d' %order_IIR)
ax[0].plot(wz_FIR, 20*np.log10(np.abs(H_FIR*ganancia)), label = 'FIR_Least-Squares_orden_%d' %cant_coeff_FIR)
ax[0].set_title('Plantilla con Respuestas de módulo')
ax[0].set_xlabel('Frecuencia [Hz]')
ax[0].set_ylabel('Amplitud [dB]')
ax[0].grid()
ax[0].set_xlim([0,100])
ax[0].set_ylim([-60,10])
ax[0].legend()

#ploteo plantilla
ax[0].fill([0, 1, 1,35,35,100,100,25,25,3,3,0],[-40,-40,5,5,-40,-40,-60,-60,0,0,-60,-60],color=[0.8,0.902,0.8])
ax[0].plot(1,-40,3,0,25,0,35,-40, marker='x', color = 'k')

#Fase
ax[1].plot(wz_IIR, np.angle(H_IIR*ganancia), label = 'fase_IIR')
ax[1].plot(wz_FIR, np.angle(H_FIR*ganancia), label = 'fase_FIR')
ax[1].set_title('Fases')
ax[1].set_xlabel('Frecuencia [Hz]')
ax[1].set_ylabel('Fase [rad]')
ax[1].grid()
ax[1].set_xlim([0,100])
ax[1].legend()

#Retardo de grupo IIR
D_IIR = -np.diff(np.angle(H_IIR))/np.diff(wz_IIR)
ax[2].plot(wz_IIR[0:(len(wz_IIR)-1)], D_IIR, label = 'Group_Delay_IIR')
ax[2].set_title('Retardos de Grupo')
ax[2].set_xlabel('Frecuencia [Hz]')
ax[2].set_ylabel('Retardo [muestras]')
ax[2].grid()
ax[2].set_xlim([0,100])
ax[2].legend()
#Retardo de grupo FIR
wz_FIR, D_FIR = sig.group_delay((coeff_FIR,1), w=wz_FIR, fs = fs)
ax[3].plot(wz_FIR, D_FIR, label = 'Group_Delay_FIR')
ax[3].set_title('Retardos de Grupo')
ax[3].set_xlabel('Frecuencia [Hz]')
ax[3].set_ylabel('Retardo [muestras]')
ax[3].grid()
ax[3].set_xlim([0,100])
ax[3].set_ylim([700,800])
ax[3].legend()

plt.tight_layout()