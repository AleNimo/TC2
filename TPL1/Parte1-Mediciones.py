# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 15:17:27 2022

@author: Alejo
"""

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

from numpy import genfromtxt


# Ajusto tamaño de graficos
mpl.rcParams['figure.figsize'] = (9,9)
mpl.rcParams['font.size'] = 15

f = np.array([1,9.35,15,25,30,40,50,60,100,10e3])

Vo = np.array([480e-3,460e-3,440e-3,340e-3,280e-3,120e-3,26e-3,148e-3,365e-3,490e-3])

Vi = np.array([490e-3,490e-3,490e-3,490e-3,490e-3,490e-3,490e-3,480e-3,490e-3,490e-3])

delta_T = np.array([0,-4.4e-3,-4.5e-3,-4.6e-3,-4.8e-3,-4.9e-3,5.2e-3,3.44e-3,1.16e-3,0])

amp = 20*np.log10(Vo/Vi)

tita  = 2*180*np.multiply(f,delta_T)

retardo_grupo = -np.diff(tita) / np.diff(f)
retardo_grupo = np.insert(retardo_grupo, 0, 0, axis = 0)


############ Graficador de BODE #######################
amplitud_CSV = genfromtxt('Amplitud.csv', delimiter=',')

f_amp2 = amplitud_CSV[:,0]
amp2 = amplitud_CSV[:,1]

fase_CSV = genfromtxt('Fase.csv', delimiter=',')

f_tita2 = fase_CSV[:,0]
tita2 = fase_CSV[:,1]

retardo_grupo2 = -np.diff(tita2) / np.diff(f_tita2)
retardo_grupo2 = np.insert(retardo_grupo2, 0, 0, axis = 0)

fig,ax = plt.subplots(3,1)

ax[0].plot(f,amp, f_amp2, amp2)
ax[0].set_xlabel('f[Hz]')
ax[0].set_ylabel(r'$|T(f)|_{[dB]}$')
ax[0].set_xscale('log')
ax[0].grid()
ax[0].set_title("Amplitud")
ax[0].legend(['Osciloscopio', 'GraficadorBode'])

ax[1].plot(f, tita, f_tita2, tita2)
ax[1].set_xlabel('f[Hz]')
ax[1].set_ylabel(r'$\theta (f)_{[°]}$')
ax[1].set_xscale('log')
ax[1].grid()
ax[1].set_title("Fase")
ax[1].legend(['Osciloscopio', 'GraficadorBode'])

ax[2].plot(f,retardo_grupo, f_tita2, retardo_grupo2)
ax[2].set_xlabel('f[Hz]')
ax[2].set_ylabel(r'$\tau (f)_{[seg]}$')
ax[2].set_xscale('log')
ax[2].grid()
ax[2].set_title("Retardo de grupo")
ax[2].legend(['Osciloscopio', 'GraficadorBode'])

fig.tight_layout()