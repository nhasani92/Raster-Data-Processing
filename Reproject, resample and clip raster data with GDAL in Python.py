# -*- coding: utf-8 -*-
"""
Created on Tue May 24 02:24:56 2022

@author: Nusrat
"""
# =============================================================================
from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
# 
ds = gdal.Open('C:/Users/Nusrat/Desktop/test/data/MOD09Q1.A2008001.h25v07.006.2015169113202_1.tif')
array = ds.GetRasterBand(1).ReadAsArray()
# # =============================================================================
plt.imshow(array)
plt.colorbar()
print(ds.GetGeoTransform())
print(ds.GetProjection())


# Reprojection
dsReprj = gdal.Warp('C:/Users/Nusrat/Desktop/test/data/demReproj', ds, dstSRS = 'EPSG:4326')
#Resample resolution
dsRes = gdal.Warp('C:/Users/Nusrat/Desktop/test/data/Res.tif', ds, XRes = 500, yRes = 500, resampleAlg = "bilinear")

#Clip Data

dsClip = gdal.Warp('C:/Users/Nusrat/Desktop/test/data/Clip.tif', ds, 
                    cutlineDSName = 'C:/Users/Nusrat/Desktop/test/data/shapefile/Tiruvannamalai_crs_100027.shp',
                    cropToCutline = True, dstNoData = np.nan)
array = ds.GetRasterBand(1).ReadAsArray()
plt.imshow(array)
plt.colorbar()
 
ds = dsClip = dsRes = dsRej = None
