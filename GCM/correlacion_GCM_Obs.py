# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 14:09:10 2024

Exploración de datos GCM contra datos Estaciones

@author: Arturo A. Granada G.
"""

import xarray as xr
import plotly.graph_objects as go
import pandas as pd
import numpy as np

r1 = 'Datos/GCM/tas_3hr_GFDL-ESM4_ssp119_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'
r2 = 'Datos/GCM/tas_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'
r3 = 'Datos/GCM/tas_3hr_GFDL-ESM4_ssp245_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'
r4 = 'Datos/UP_5.csv'

'''Carga datos GCM (netCDF)'''
ds1 = xr.open_dataset(r1)
ds2 = xr.open_dataset(r2)
ds3 = xr.open_dataset(r3)

'''Carga datos Estaciones (CSV)'''
ds4 = pd.read_csv(r4, sep=';')
ds4['Fecha'] = pd.to_datetime(ds4['Fecha'], format='%Y-%m-%d %H:%M:%S')

'''Seleccionamos las variables y periodo de estudio'''
f_i = '2015-01-01 03:00'
f_f = '2023-03-16 18:00'

temp_GFDL_119 = ds1['tas'].loc[f_i:f_f]
temp_GFDL_126 = ds2['tas'].loc[f_i:f_f]
temp_GFDL_245 = ds3['tas'].loc[f_i:f_f]

temp_estacion = ds4.loc[~((ds4['Fecha'].dt.month == 2) & (ds4['Fecha'].dt.day == 29))]
temp_estacion.set_index('Fecha', inplace=True)
temp_estacion = temp_estacion.resample('3h').mean().reset_index()

''' Seleccionamos pixel de interes'''
lon_GCM = 283.1
lat_GCM = 3.5
t_GCM_119 = temp_GFDL_119.sel(lon=lon_GCM, lat=lat_GCM, method='nearest')
t_GCM_126 = temp_GFDL_126.sel(lon=lon_GCM, lat=lat_GCM, method='nearest')
t_GCM_245 = temp_GFDL_245.sel(lon=lon_GCM, lat=lat_GCM, method='nearest')

'''Convertimos a DF'''
temp_GCM_119 = t_GCM_119.to_dataframe().reset_index() 
temp_GCM_126 = t_GCM_126.to_dataframe().reset_index()
temp_GCM_245 = t_GCM_245.to_dataframe().reset_index()

cor_person_119 = temp_GCM_119['tas'].corr(temp_estacion['Tmedia'])
cor_spearman_119 = temp_GCM_119['tas'].corr(temp_estacion['Tmedia'], method='spearman')
cor_person_126 = temp_GCM_126['tas'].corr(temp_estacion['Tmedia'])
cor_spearman_126 = temp_GCM_126['tas'].corr(temp_estacion['Tmedia'], method='spearman')
cor_person_245 = temp_GCM_245['tas'].corr(temp_estacion['Tmedia'])
cor_spearman_245 = temp_GCM_245['tas'].corr(temp_estacion['Tmedia'], method='spearman')

print(f'Correlación Pearson 119: {cor_person_119}')
print(f'Correlación Pearson 126: {cor_person_126}')
print(f'Correlación Pearson 245: {cor_person_245}')
print('....................................................')
print(f'Correlación Sperman 119: {cor_spearman_119}')
print(f'Correlación Sperman 126: {cor_spearman_126}')
print(f'Correlación Sperman 245: {cor_spearman_245}')