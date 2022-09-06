# -*- coding: utf-8 -*-
"""
Created on Mon May 23 15:57:16 2022

@author: Nusrat
"""

import geopandas as gpd

# Importing shapefile and plotting color
state = gpd.read_file(r'C:/Users/Nusrat/Desktop/test/data/shapefile/india_states/india_states.shp')
state.plot(cmap = 'hsv', edgecolor = 'black', column = 'stname')

area = gpd.read_file(r'C:/Users/Nusrat/Desktop/test/data/shapefile/Tiruvannamalai_crs_100027.shp')
area.plot(cmap = 'jet')                   

#Plot the figures side by side
