# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 14:09:10 2024

Exploración de datos GCM contra datos ERA5-Land

@author: Arturo A. Granada G.
"""

import xarray as xr
import plotly.graph_objects as go
import pandas as pd
import numpy as np

r1 = 'Datos/GCM/tas_3hr_GFDL-ESM4_ssp119_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'
r2 = 'Datos/GCM/tas_3hr_GFDL-ESM4_ssp245_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'
r3 = 'Datos/ERA5_Land_T_P/ERA5-Land_2015_2023_ValleDelCauca_3H.nc'

ds1 = xr.open_dataset(r1)
ds2 = xr.open_dataset(r2)
ds3 = xr.open_dataset(r3)

''' Promediamos por día'''
dia_GCM119 = ds1.resample(time='12h').mean()
dia_GCM245 = ds2.resample(time='12h').mean()
dia_Era = ds3.resample(time='12h').mean()

'''Seleccionamos las variables y periodo de estudio'''
f_i = '2015-01-01 03:00'
f_f = '2023-12-31 21:00'

temp_GFDL_119 = ds1['tas'].loc[f_i:f_f]
temp_GFDL_245 = ds2['tas'].loc[f_i:f_f]
temp_ERA = ds3['t2m'].loc[f_i:f_f]
temp_ERA = temp_ERA.loc[~((temp_ERA['time'].dt.month == 2) & (temp_ERA['time'].dt.day== 29))]

temp_119_dia = dia_GCM119['tas'].loc[f_i:f_f]
temp_245_dia = dia_GCM245['tas'].loc[f_i:f_f]
temp_ERA_dia = dia_Era['t2m'].loc[f_i:f_f]
temp_ERA_dia = temp_ERA_dia.loc[~((temp_ERA_dia['time'].dt.month == 2) & (temp_ERA_dia['time'].dt.day== 29))]

''' Seleccionamos pixel de interes'''
lon_GCM = 283.1
lat_GCM = 3.5

lon_ERA_cumbre = -76.9869 #-76.5647
lat_ERA_cumbre = 3.8480 #3.6451



t_GCM = temp_GFDL_119.sel(lon=lon_GCM, lat=lat_GCM, method='nearest')
t_GCM_245 = temp_GFDL_245.sel(lon=lon_GCM, lat=lat_GCM, method='nearest')
t_ERA_cumbre = temp_ERA.sel(longitude=lon_ERA_cumbre, latitude=lat_ERA_cumbre, method='nearest')

temp_Era_cumbre = t_ERA_cumbre.to_dataframe()#.reset_index() 
temp_GCM_cumbre = t_GCM.to_dataframe()#.reset_index() 
temp_GCM245_cumbre = t_GCM_245.to_dataframe()

def k_c (k):
    c = k - 273.15
    return c

temp_Era_cumbre['t2m'] = temp_Era_cumbre['t2m'].apply(k_c)
temp_GCM_cumbre['tas'] = temp_GCM_cumbre['tas'].apply(k_c)
temp_GCM245_cumbre['tas'] = temp_GCM245_cumbre['tas'].apply(k_c)

''' Plot con Plotly'''
fig = go.Figure()

''' Agregar datos de temperatura'''
fig.add_trace(go.Scatter(x = temp_Era_cumbre.index, y = temp_Era_cumbre['t2m'], mode='lines', name='ERA5-Land La Cumbre', line=dict(color='#3366CC')))
fig.add_trace(go.Scatter(x = temp_GCM_cumbre.index, y = temp_GCM_cumbre['tas'], mode='lines', name='GFDL SSP1-1.9', line=dict(color='#DC3912')))
fig.update_layout(title = 'Temperatura GFDL SSP2-2.5 vs Observaciones "ERA5-Land"',
                  title_font_size=22,
                  legend=dict(title="Altura: 1613 m.s.n.m"),
                  xaxis_title = 'Tiempo (3h)',
                  yaxis_title = 'Temperatura °C',
                  template='seaborn')
fig.show()

#temp_Era_cumbre.to_csv('ERA_pacifico_3h.csv', sep=';')
#temp_GCM_cumbre.to_csv('GCM119_pacifico_dia.csv', sep=';')
#temp_GCM245_cumbre.to_csv('GCM245_pacifico_dia.csv', sep=';')

#correlacion_GCM_ERA_cumbre = a.corr(b)
#print(f'Correlación GCM 119 vs ERA5-Land: {correlacion_GCM_ERA_cumbre}')