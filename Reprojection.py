# -*- coding: utf-8 -*-
"""
Created on Mon May 23 16:19:43 2022

@author: Nusrat
"""

from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt

ds = gdal.Open("C:/Users/Nusrat/Desktop/test/data/MOD09Q1.A2008001.h25v07.006.2015169113202_1.tif")
array = ds.ReadAsArray()
plt.imshow(array)
plt.colorbar()
print(ds.GetGeoTransform())
print(ds.GetProjection())

# =============================================================================
# dsReprj = gdal.Warp("C:/Users/Nusrat/Desktop/test/data/Reprj.tif", 'EPSG:4326")
# =============================================================================
# =============================================================================
# output_raster = r"C:/Users/Nusrat/Desktop/test/data"
# =============================================================================
# =============================================================================
# warp = gdal.Warp('Raster_Pro', 'EPSG:4326')
# =============================================================================
