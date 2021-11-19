# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 16:39:54 2021

@author: phmar
"""

import control 
from control import TransferFunction
import numpy as np

s = TransferFunction.s

eta = 0.7
wn1 = 0.4
wn2 = 0.63
wn3 = 1

nwn2 = 0.52124
nwn1 = nwn2 - 0.23
nwn3 = nwn2 + 0.37

"""H = TransferFunction([1, 2*eta*wn1, wn1**2],[1, 2*wn1, wn1**2])
print(H)

G = TransferFunction([1, 2*eta*wn2, wn2**2],[1, 2*wn2, wn2**2])
print(G)

I = TransferFunction([1, 2*eta*wn3, wn3**2],[1, 2*wn3, wn3**2])
print(I)"""

H = TransferFunction([1, 2*eta*nwn1, nwn1**2],[1, 2*nwn1, nwn1**2])
print(H)

G = TransferFunction([1, 2*eta*nwn2, nwn2**2],[1, 2*nwn2, nwn2**2])
print(G)

I = TransferFunction([1, 2*eta*nwn3, nwn3**2],[1, 2*nwn3, nwn3**2])
print(I)

HGI = H*G*I
print(HGI)


Teste = TransferFunction([1, 2.385, 2.868, 1.892, 0.758, 0.1659, 0.0183],[1, 3.407, 4.655, 3.255, 1.228, 0.237, 0.0183])
Teste2 = TransferFunction([1, 2.842, 4.07, 3.277, 1.623, 0.4523, 0.0635],[1, 4.06, 6.685, 5.709, 2.667, 0.6461, 0.0635])
