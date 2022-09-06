# -*- coding: utf-8 -*-
"""
Created on Mon May 23 23:54:07 2022

@author: Nusrat
"""

from osgeo import gdal

filename = r"C:/Users/Nusrat/Desktop/test/data/MOD09Q1.A2008001.h25v07.006.2015169113202_1.tif"
input_raster = gdal.Open('new_data')
output_raster = r"C:/Users/Nusrat/Desktop/test/data/new_data.tif"
warp = gdal.Warp(output_raster,input_raster,dstSRS='EPSG:4326')
warp = None