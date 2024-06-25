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
r2 = 'Datos/GCM/tas_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'
r3 = 'Datos/GCM/tas_3hr_GFDL-ESM4_ssp245_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'
#r4 = 'Datos/ERA5_Land_T_P/ERA5-Land_2015_2023_ValleDelCauca_3H.nc'

ds1 = xr.open_dataset(r1)
ds2 = xr.open_dataset(r2)
ds3 = xr.open_dataset(r3)
#ds4 = xr.open_dataset(r4)

''' Promediamos por día'''
dia_GCM119 = ds1.resample(time='12h').mean()
dia_GCM126 = ds2.resample(time='12h').mean()
dia_GCM245 = ds3.resample(time='12h').mean()
#dia_Era = ds4.resample(time='12h').mean()

'''Seleccionamos las variables y periodo de estudio'''
f_i = '2015-01-01 03:00'
f_f = '2023-12-31 21:00'

temp_GFDL_119 = ds1['tas'].loc[f_i:f_f]
temp_GFDL_126 = ds2['tas'].loc[f_i:f_f]
temp_GFDL_245 = ds3['tas'].loc[f_i:f_f]
#temp_ERA = ds4['t2m'].loc[f_i:f_f]
#temp_ERA = temp_ERA.loc[~((temp_ERA['time'].dt.month == 2) & (temp_ERA['time'].dt.day== 29))]

##temp_119_dia = dia_GCM119['tas'].loc[f_i:f_f]
##temp_245_dia = dia_GCM245['tas'].loc[f_i:f_f]
##temp_ERA_dia = dia_Era['t2m'].loc[f_i:f_f]
##temp_ERA_dia = temp_ERA_dia.loc[~((temp_ERA_dia['time'].dt.month == 2) & (temp_ERA_dia['time'].dt.day== 29))]

''' Seleccionamos pixel de interes'''
lon_GCM = 283.1
lat_GCM = 3.5

lon_ERA_cumbre = -76.5647
lat_ERA_cumbre = 3.6451

lon_ERA_pacifico = -76.9869 #-76.5647
lat_ERA_pacifico = 3.8480 #3.6451

t_GCM_119 = temp_GFDL_119.sel(lon=lon_GCM, lat=lat_GCM, method='nearest')
t_GCM_126 = temp_GFDL_126.sel(lon=lon_GCM, lat=lat_GCM, method='nearest')
t_GCM_245 = temp_GFDL_245.sel(lon=lon_GCM, lat=lat_GCM, method='nearest')
#t_ERA_cumbre = temp_ERA.sel(longitude=lon_ERA_cumbre, latitude=lat_ERA_cumbre, method='nearest')
#t_ERA_pacifico = temp_ERA.sel(longitude=lon_ERA_pacifico, latitude=lat_ERA_pacifico, method='nearest')


temp_GCM_119 = t_GCM_119.to_dataframe()#.reset_index() 
temp_GCM_126 = t_GCM_126.to_dataframe()
temp_GCM_245 = t_GCM_245.to_dataframe()

#temp_Era_cumbre = t_ERA_cumbre.to_dataframe()#.reset_index() 
#temp_Era_pacifico = t_ERA_pacifico.to_dataframe()

def k_c (k):
    c = k - 273.15
    return c

temp_GCM_119['tas'] = temp_GCM_119['tas'].apply(k_c)
temp_GCM_126['tas'] = temp_GCM_126['tas'].apply(k_c)
temp_GCM_245['tas'] = temp_GCM_245['tas'].apply(k_c)

temp_GCM_SSP = pd.concat([temp_GCM_119['tas'], temp_GCM_126['tas'], temp_GCM_245['tas']], axis=1)
temp_GCM_SSP = temp_GCM_SSP.rename(index={ 1: 'tas119', 2: 'tas126', 3: 'tas245'})
print(temp_GCM_SSP)

#temp_Era_cumbre['t2m'] = temp_Era_cumbre['t2m'].apply(k_c)
#temp_Era_pacifico['t2m'] = temp_Era_pacifico['t2m'].apply(k_c)

''' Uniendo '''

''' Plot con Plotly'''
#fig = go.Figure()

''' Agregar datos de temperatura'''
#fig.add_trace(go.Scatter(x = temp_Era_cumbre.index, y = temp_Era_cumbre['t2m'], mode='lines', name='ERA5-Land La Cumbre', line=dict(color='#636EFA')))
#fig.add_trace(go.Scatter(x = temp_Era_pacifico.index, y = temp_Era_pacifico['t2m'], mode='lines', name='ERA5-Land U. Pacífico', line=dict(color='#EF553B')))

#fig.add_trace(go.Scatter(x = temp_GCM_119.index, y = temp_GCM_119['tas'], mode='lines', name='GFDL SSP1-1.9', line=dict(color='#109618')))
#fig.add_trace(go.Scatter(x = temp_GCM_126.index, y = temp_GCM_126['tas'], mode='lines', name='GFDL SSP1-2.6', line=dict(color='#FF9900')))
#fig.add_trace(go.Scatter(x = temp_GCM_245.index, y = temp_GCM_245['tas'], mode='lines', name='GFDL SSP2-4.5', line=dict(color='#DC3912')))
#fig.update_layout(title = 'Temperatura estimada GFDL vs "ERA5-Land"',
#                  title_font_size=22,
#                  legend=dict(title="U. Pacifico: 16 m.s.n.m - La cumbre: 1613 m.s.n.m"),
#                  xaxis_title = 'Tiempo (3h)',
#                  yaxis_title = 'Temperatura °C',
#                  template='seaborn')
#fig.show()

#temp_Era_cumbre.to_csv('ERA_pacifico_3h.csv', sep=';')
#temp_GCM_cumbre.to_csv('GCM119_pacifico_dia.csv', sep=';')
#temp_GCM245_cumbre.to_csv('GCM245_pacifico_dia.csv', sep=';')

#correlacion_GCM_ERA_cumbre = a.corr(b)
#print(f'Correlación GCM 119 vs ERA5-Land: {correlacion_GCM_ERA_cumbre}')