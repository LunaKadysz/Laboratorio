# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:16:06 2019

@author: Publico
"""

import numpy as np
import pyvisa as visa

#%% Me conecto con el osciloscopio
#Creo la interfaz visa para comunicarme con equipos
rm = visa.ResourceManager()
#Pregunto que dispositvos están conectados
print(rm.list_resources())
rscosci = rm.list_resources('USB::0x0699::0x0368::?*::INSTR')[0]

#Abro la comunicación con los equipos (Osc Tektronik TBS 1052B-EDU)
osci = rm.open_resource(rscosci)
print(osci.query('*IDN?'))

#Eligo el modo de transmisión de datos (binario)
osci.write('DAT:ENC RPB')
osci.write('DAT:WID 1')
'''
The range is 0 to 255 when DATa:WIDth is 1. Center screen is 127. The range is
0 to 65,535 when DATa:WIDth is 2. The upper limit is one division above the top
of the screen and the lower limit is one division below the bottom of the screen.
'''

#%% Me conecto con el generador y con el osciloscopio


#Código para leer los valores que mide el osciloscopio ()


osci.query('measu:immed?') #Le pregunto qué es lo que está midiendo
osci.write('measu:immed:type pk2pk') #Seteo para que mida Vpp
osci.write('measu:immed:source ch1') #Seteo para que mida el canal 1
print(osci.query('measu:immed:value?'))#Le pido el valor, en este caso de Vp, pero de lo que haya seteado
print(osci.query('measu:immed:units?'))#Le pido las unidades
#Otras valores que le puedo pedir
osci.write('measu:immed:type phase') #fase (un canal es 0 por definición, el otro es la diferencia)
osci.write('measu:immed:type rms') #Vrms
'''
El resto de los parametros los pueden sacar del manual de programación
del osciloscopio bajo el título MEASUrement:IMMed:TYPe
(sugerencia, usen el ctrl+f) 
'''

#También puedo medir en el canal 2
osci.write('measu:immed:source ch2')