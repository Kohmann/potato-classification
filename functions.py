#!/usr/bin/env python
# coding: utf-8


import numpy as np
from spectral import principal_components
import matplotlib.pyplot as plt


def plotSpectrum(arr, xaxis="wavelength", linelabel=0 ):

    if xaxis == "wavelength":
        x = np.linspace(400,1000,len(arr))
    elif xaxis == "band":
        x = np.linspace(0,len(arr), len(arr))
        
    else:
        print("xaxis wasnt wavelength or band")
        return 0
    
    if linelabel != 0:
        plt.plot(x, arr, label=linelabel)
        plt.legend()
    else: 
        plt.plot(x, arr)
    plt.ylabel("Reflectance")
    plt.xlabel(xaxis)
    


    

def PCAreduce(img, frac=0.999):
    
    pc = principal_components(img)
    reduced = pc.reduce(fraction=frac)
    
    return reduced.transform(img), reduced.eigenvalues

def clip(img, mi, ma):
    """
    Clips values in between min and max
    Values bigger then max gets set equal to 0
    """
    for i in range(img.shape[2]):
        img[:,:,i][img[:,:,i] > ma] = 0
        img[:,:,i][img[:,:,i] < mi] = 0

    return 0