
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:48:41 2019

@author: Publico
"""
import numpy as np
import pyvisa as visa
import matplotlib.pyplot as plt

rm = visa.ResourceManager()
rscosci = rm.list_resources('USB::0x0699::0x0368::C017046::INSTR')[0]#Version automatica par conectar
osci = rm.open_resource('USB0::0x0699::0x0368::C017046::INSTR')


Voltaje= np.array([])
Fase=np.array([])
Rms= np.array([])
osci.write('measu:immed:source ch1') #Seteo para que mida el canal 1   
osci.write('measu:immed:type pk2pk')
Voltaje = np.append(Voltaje,osci.query_ascii_values('measu:immed:value?'))
osci.write('measu:immed:type phase') #fase (un canal es 0 por definición, el otro es la diferencia)
Fase = np.append(Fase,osci.query_ascii_values('measu:immed:value?'))
osci.write('measu:immed:type rms') #Vrms
Rms = np.append(Rms,osci.query_ascii_values('measu:immed:value?'))

freq = np.logspace(2,4,25) 

T=[]
A=[]

w_c=16000

def Transmición(x):
    y=1/((1+(x/w_c)**2)**(1/2))
    if len(T)!=25:
        T.append(y)
    return y
plt.xscale(value="log")    
plt.plot(freq, [Transmición(i) for i in freq], 'ko')

def Atenuación(x):
    y= 20*np.log10(x)
    if len(A)!=25:
        A.append(y)
    return y

plt.xscale(value="log")
plt.plot(freq, [Atenuación(i) for i in T], 'go')

Desfasaje=[]
    
def Fase(x):
    y=-np.arctan(x/w_c)
    if len(Desfasaje)!=25:
        Desfasaje.append(y)
    return y
plt.xscale(value="log")
plt.plot(freq, [Fase(i) for i in freq], 'ro')
