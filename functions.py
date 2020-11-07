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

def meanSpectrum(cube):  # works only for subregions
    bands = cube.shape[2]
    avgSpec = np.zeros(bands)    
    for i in range(bands):
        avgSpec[i] = cube[:,:,i].mean()
    return avgSpec

def getImage(time):
    files = [ "../Strawberry/Normalised/STR_B1_before-hit_VNIR_1800_SN00841_HSNR2_11998us_2020-08-02T184054_raw_rad_nn.hdr",
             "../Strawberry/Normalised/STR_B1_0mn_VNIR_1800_SN00841_HSNR2_11998us_2020-08-02T185621_raw_rad_nn.hdr",
             "../Strawberry/Normalised/STR_B1_30min_VNIR_1800_SN00841_HSNR2_11998us_2020-08-02T193019_raw_rad_nn.hdr",
             "../Strawberry/Normalised/STR_B1_1hr_VNIR_1800_SN00841_HSNR2_11998us_2020-08-02T202126_raw_rad_nn.hdr",
             "../Strawberry/Normalised/STR_B1_3hr_VNIR_1800_SN00841_HSNR2_11998us_2020-08-02T214153_raw_rad_nn.hdr",
             "../Strawberry/Normalised/STR_B1_12h_VNIR_1800_SN00841_HSNR2_9998us_2020-08-03T112003_raw_rad_nn.hdr",
             "../Strawberry/Normalised/STR_B1_24h_VNIR_1800_SN00841_HSNR2_9998us_2020-08-03T181621_raw_rad_nn.hdr",
             "../Strawberry/Normalised/STR_B1_48h_VNIR_1800_SN00841_HSNR2_9998us_2020-08-04T152605_raw_rad_nn.hdr"
            ]
    time = "_" + time # string must have _ in front to make it unique
    for file in files:
        if time in file:
            return file
    
    print('Format must be [before_hit, 0m, 30m, 1h, 3h, 12h, 24h, 48h]')
    return 0


def getRegion(img, x=0, y=0, kernel=1):
    if (not x or not y):
        print("Format is [image, x-coord, y-coord, kernel]")
    elif (x and y):
        return img.read_subregion((y - kernel//2, y + kernel//2 + 1),
                              (x - kernel//2, x + kernel//2 + 1))