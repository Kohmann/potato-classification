#!/usr/bin/env python
# coding: utf-8


import numpy as np
import matplotlib.pyplot as plt



def plotSpectrum(arr, xaxis="wavelength"):

    if xaxis == "wavelength":
        x = np.linspace(400,1000,len(arr))
    elif xaxis == "band":
        x = np.linspace(0,len(arr), len(arr))
        
    else:
        print("xaxis wasnt wavelength or band")
        return 0
    
    plt.plot(x, arr)
    plt.ylabel("Reflectance")
    plt.xlabel(xaxis)
