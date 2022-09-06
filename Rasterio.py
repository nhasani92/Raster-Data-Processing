# -*- coding: utf-8 -*-
"""
Created on Tue May 24 12:24:13 2022

@author: Nusrat
"""

import rasterio
import numpy as np
import matplotlib.pyplot as plt

#Reading raster data

in_img = r'C:/Users/Nusrat/Desktop/test/data/MOD09Q1.A2008001.h25v07.006.2015169113202_1.tif'

ds = rasterio.open(in_img)
ds

data = ds.read()

#Reading meta data

ds.meta

ds.name

ds.count

ds.shape

ds.width

ds.height

ds.driver

ds.transform

ds.crs

ds. description

data.size

data.type

data.min()

data.dtype

data.max()

#Visualizing raster data

from rasterio.plot import show, show_hist

show_hist(ds, cmaps="Spectral", title='MOIDS')


