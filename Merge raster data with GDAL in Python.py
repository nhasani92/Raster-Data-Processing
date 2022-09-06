# -*- coding: utf-8 -*-
"""
Created on Tue May 24 03:19:45 2022

@author: Nusrat
"""

from osgeo import gdal
import glob
import subprocess

# list all files in directory that match pattern
demList = glob.glob('C:/Users/Nusrat/Desktop/test/data [0-9][0-9].tif')
print(demList)

# gdal_merge
cmd = "gdal_merge.py -ps 10 -10 -o mergedDEM.tif"
subprocess.call(cmd.split()+demList)

# build virtual raster and convert to geotiff
vrt = gdal.BuildVRT("merged.vrt", demList)
gdal.Translate("mergedDEM2.tif", vrt, xRes = 10, yRes = -10)
vrt = None