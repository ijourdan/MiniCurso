import numpy as np


def modula(t, ruido=False):
    if ruido:
        tiempo_del_dato = t.max()/5
        fase_inicial = 2 * np.pi * np.random.rand()
        
        # sin dato
        mu0 = 300 
        sigma0 = 70
        freq0 = sigma0 * np.random.randn() + mu0
        # con dato
        mu1 = 500
        sigma1 = 100
        freq1 = sigma1 * np.random.randn() + mu1
        minimo = np.random.rand()*(t.max() - tiempo_del_dato) # donde empieza el dato
        rango_del_dato = (minimo <= t) & (t <= minimo+ tiempo_del_dato)
        
        #base_line
        out = 2 * np.pi * freq0 * t + fase_inicial
        out[rango_del_dato] = 2 * np.pi * freq1 * t[rango_del_dato] + fase_inicial
        
    else:
        tiempo_del_dato = t.max()/5
        rango_del_dato = (2 * tiempo_del_dato <= t) & (t <= 3 * tiempo_del_dato)
        out = 2 * np.pi * 300 * t
        out[rango_del_dato] = 2 * np.pi * 500 * t[rango_del_dato]
    return out