# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:29:17 2024

Extración variables ERA5-Land con coordenadas (estaciones meteorologicas)

@author: Arturo A. Granada G.
"""

import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

''' 1. Cargar el conjunto de datos CMIP6 (ejemplo: temperatura media diaria) '''

r =  'Datos/ERA5_Land_T_P/ERA5-Land_2015_2023_ValleDelCauca.nc'
rp = 'Datos/ERA5_Land_T_P/ERA5-Land_2015_2023_ValleDelCauca_Hora.nc'
ds = xr.open_dataset(r)
dsp = xr.open_dataset(rp)

'''Transformar la fecha del netCDF'''
ds['time'] = ds.indexes['time']#.to_datetime().index()
dsp['time'] = ds.indexes['time']
''' 3. Cargamos los datos de temperatura del DataSet'''
tas = ds['t2m'] - 273.15
tas.attrs['units'] = '°C' #Cambiamos el argumento a °C

''' 4. Cargamos los datos de temperatura del DataSet'''
pr = dsp['tp'] / 0.01
#pr.attrs['units'] = '°C' #Cambiamos el argumento a °C

''' Seleccionamos pixel de interes'''
lon = -76.65138 #Longitud del pixel
lat = 3.41583 #Latitud del pixel (Mirarlo en en el DF cortado)
lon_ERA_arpto = -76.3822
lat_ERA_arpto = 3.5327

lon_ERA_farallones = -76.6513
lat_ERA_farallones = 3.4158

lon_ERA_cumbre = -76.5647
lat_ERA_cumbre = 3.6451

lon_ERA_diana = -76.1855
lat_ERA_diana = 3.3138

lon_ERA_siloe = -76.5605
lat_ERA_siloe = 3.4252

lon_ERA_univalle = -76.5338
lat_ERA_univalle = 3.3777

lon_ERA_pacifico = -76.9869
lat_ERA_pacifico = 3.8480 

temp_estacion = tas.sel(longitude = lon_ERA_pacifico, latitude = lat_ERA_pacifico, method='nearest')
prec_estacion = pr.sel(longitude = lon_ERA_pacifico, latitude = lat_ERA_cumbre, method='nearest')

'''Convertimos a DF'''
df_temp = temp_estacion.to_dataframe().reset_index()
df_prec = prec_estacion.to_dataframe().reset_index()

df_temp.to_csv('Temp_ERA5_Pacifico.csv', sep=';', index=True)
df_prec.to_csv('Prec_ERA5_Pacifico.csv', sep=';', index=True)
print(df_temp)
print('Proceso finalizado.')