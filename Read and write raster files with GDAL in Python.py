# -*- coding: utf-8 -*-
"""
Created on Tue May 24 01:25:11 2022

@author: Nusrat
"""

from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt

ds = gdal.Open("C:/Users/Nusrat/Desktop/test/data/DEM_Compress/DEM_NCR.tif")
gt = ds.GetGeoTransform()
proj = ds.GetProjection()

band = ds.GetRasterBand(1)
array = band.ReadAsArray()

# =============================================================================
# plt.figure()
# plt.imshow(array)
# =============================================================================

binmask = np.where((array >= np.mean(array)),1,0)
# =============================================================================
# plt.figure()
# plt.imshow(binmask)
# =============================================================================

#Export data
driver = gdal.GetDriverByName("GTiff")
driver.Regsiter()
outds = driver.Create("binmask.tif", xszie = binmask.shape[1], ysize = binmask.shape[0], bands =1, eType = gdal.GDT_Int32)
outds.SetGeoTransform(gt)
outds.SetProjection(proj)
outband = outds.GetRasterBand(1)
outband.WriteArray(binmask)
outband.SetNoDatavalue(np.nan)
outband.FlushCache()

outband =  None
outds = None