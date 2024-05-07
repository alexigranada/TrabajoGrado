# -*- coding: utf-8 -*-
"""
Created on Sun May 05 14:45:03 2024

Exploración de datos de precipitación de CHIRPS

@author: Arturo A. Granada G.
"""

import pandas as pn
import geopandas as gpn
import xarray as xr
import plotly.graph_objects as go
import rasterio
from rasterio.transform import from_origin
from rasterio.enums import Resampling
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from shapely.geometry import box
import cartopy.crs as ccrs
import numpy as np
import cmocean
import cftime
import datetime

''' 1. Cargar el conjunto de datos CMIP6 (ejemplo: temperatura media diaria) '''
ruta = 'Datos/Estaciones/IDEAM/Hora/CHIRPS Dia Valle/data.nc'
ds = xr.open_dataset(ruta)
print(ds)

precipitacion = ds['prcp']
#print(precipitacion['X'])
#print(precipitacion['Y'])

''' Seleccionamos pixel de interes'''
lat_1 = 3.675 #Latitud del pixel (Mirarlo en en el DF cortado)
lon_1 = -76.525 #Longitud del pixel

'''Seleccionamos pixel con el método 'Valor más cercano' '''
preci = precipitacion.sel(X=lon_1, Y=lat_1, method = None)# 

df_prec = preci.to_dataframe().reset_index() #Convertimos a DF
print(df_prec)

''' Exportar el DataFrame a un archivo CSV '''
title = f'CHIRPS_Top-Right_LaCumbre_Dia.csv'
df_prec.to_csv(title, sep=';', index=False)
