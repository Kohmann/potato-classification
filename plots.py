#!/usr/bin/env python
# coding: utf-8


import numpy as np
import matplotlib.pyplot as plt



def plotSpectrum(arr):
    x = np.linspace(400,1000,len(arr))
    plt.plot(x,arr)
    plt.ylabel("Reflectanse")
    plt.xlabel("Wavelength")
