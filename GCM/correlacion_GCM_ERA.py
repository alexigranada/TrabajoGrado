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

#r1 = 'Datos/GCM/tas_3hr_GFDL-ESM4_ssp119_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'
#r2 = 'Datos/GCM/tas_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'
#r3 = 'Datos/GCM/tas_3hr_GFDL-ESM4_ssp245_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'
r1 = 'Datos/GCM/pr_3hr_GFDL-ESM4_ssp119_r1i1p1f1_gr1_201501010130-203412312230_ValleDelCauca.nc'
r2 = 'Datos/GCM/pr_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010130-203412312230_ValleDelCauca.nc'
r3 = 'Datos/GCM/pr_3hr_GFDL-ESM4_ssp245_r1i1p1f1_gr1_201501010130-203412312230_ValleDelCauca.nc'
r4 = 'Datos/ERA5_Land_T_P/ERA5-Land_2015_2023_ValleDelCauca_3H.nc'

ds1 = xr.open_dataset(r1)
ds2 = xr.open_dataset(r2)
ds3 = xr.open_dataset(r3)
ds4 = xr.open_dataset(r4)

''' Promediamos por día'''
#dia_GCM119 = ds1.resample(time='YE').mean()
#dia_GCM126 = ds2.resample(time='D').mean()
#dia_GCM245 = ds3.resample(time='D').mean()
#dia_Era = ds4.resample(time='YE').mean()

'''Seleccionamos las variables y periodo de estudio'''
f_i = '2015-01-01 03:00'
f_f = '2023-12-31 21:00'


temp_GFDL_119 = ds1['pr'].loc[f_i:f_f]
temp_GFDL_126 = ds2['pr'].loc[f_i:f_f]
temp_GFDL_245 = ds3['pr'].loc[f_i:f_f]
temp_ERA = ds4['tp'].loc[f_i:f_f]
temp_ERA = temp_ERA.loc[~((temp_ERA['time'].dt.month == 2) & (temp_ERA['time'].dt.day == 29))]

##temp_119_dia = dia_GCM119['tas'].loc[f_i:f_f]
##temp_245_dia = dia_GCM245['tas'].loc[f_i:f_f]
##temp_ERA_dia = dia_Era['t2m'].loc[f_i:f_f]
##temp_ERA_dia = temp_ERA_dia.loc[~((temp_ERA_dia['time'].dt.month == 2) & (temp_ERA_dia['time'].dt.day== 29))]

''' Seleccionamos pixel de interes'''
lon_GCM = 283.1
lat_GCM = 3.5

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

lon_ERA_pacifico = -76.9869 #-76.5647
lat_ERA_pacifico = 3.8480 #3.6451

t_GCM_119 = temp_GFDL_119.sel(lon=lon_GCM, lat=lat_GCM, method='nearest')
t_GCM_126 = temp_GFDL_126.sel(lon=lon_GCM, lat=lat_GCM, method='nearest')
t_GCM_245 = temp_GFDL_245.sel(lon=lon_GCM, lat=lat_GCM, method='nearest')
t_ERA_arpto = temp_ERA.sel(longitude=lon_ERA_arpto, latitude=lat_ERA_arpto, method='nearest')
t_ERA_farallones = temp_ERA.sel(longitude=lon_ERA_farallones, latitude=lat_ERA_farallones, method='nearest')
t_ERA_cumbre = temp_ERA.sel(longitude=lon_ERA_cumbre, latitude=lat_ERA_cumbre, method='nearest')
t_ERA_diana = temp_ERA.sel(longitude=lon_ERA_diana, latitude=lat_ERA_diana, method='nearest')
t_ERA_siloe = temp_ERA.sel(longitude=lon_ERA_siloe, latitude=lat_ERA_siloe, method='nearest')
t_ERA_univalle = temp_ERA.sel(longitude=lon_ERA_univalle, latitude=lat_ERA_univalle, method='nearest')
t_ERA_pacifico = temp_ERA.sel(longitude=lon_ERA_pacifico, latitude=lat_ERA_pacifico, method='nearest')


temp_GCM_119 = t_GCM_119.to_dataframe().reset_index() 
temp_GCM_126 = t_GCM_126.to_dataframe().reset_index()
temp_GCM_245 = t_GCM_245.to_dataframe().reset_index()

temp_Era_arpto = t_ERA_arpto.to_dataframe().reset_index()
temp_Era_farallones = t_ERA_farallones.to_dataframe().reset_index()
temp_Era_cumbre = t_ERA_cumbre.to_dataframe().reset_index()
temp_Era_diana = t_ERA_diana.to_dataframe().reset_index()
temp_Era_siloe = t_ERA_siloe.to_dataframe().reset_index()
temp_Era_univalle = t_ERA_univalle.to_dataframe().reset_index() 
temp_Era_pacifico = t_ERA_pacifico.to_dataframe().reset_index()

def correlacion (df1, x, df2, y):
    cor_person = df1[x].corr(df2[y])
    cor_spearman = df1[x].corr(df2[y], method='spearman')
    return { 'pearson': cor_person, 'spearman': cor_spearman }

print('La univalle')
res_119 = correlacion(temp_Era_univalle, 'tp', temp_GCM_119, 'pr')
print(f'La correlacion person 119 es: {res_119['pearson']}')
print(f'La correlacion spearman 119 es: {res_119['spearman']}')

res_126 = correlacion(temp_Era_univalle, 'tp', temp_GCM_126, 'pr')
print(f'La correlacion person 126 es: {res_126['pearson']}')
print(f'La correlacion spearman 126 es: {res_126['spearman']}')

res_245 = correlacion(temp_Era_univalle, 'tp', temp_GCM_245, 'pr')
print(f'La correlacion person 245 es: {res_245['pearson']}')
print(f'La correlacion spearman 245 es: {res_245['spearman']}')

#cor_person_Cumbre_119 = temp_Era_cumbre['tp'].corr(temp_GCM_119['pr'])
#cor_spearman_Cumbre_119 = temp_Era_cumbre['tp'].corr(temp_GCM_119['pr'], method='spearman')
#cor_person_Cumbre_126 = temp_Era_cumbre['t2m'].corr(temp_GCM_126['tas'])
#cor_spearman_Cumbre_126 = temp_Era_cumbre['t2m'].corr(temp_GCM_126['tas'], method='spearman')
#cor_person_Cumbre_245 = temp_Era_cumbre['t2m'].corr(temp_GCM_245['tas'])
#cor_spearman_Cumbre_245 = temp_Era_cumbre['t2m'].corr(temp_GCM_245['tas'], method='spearman')

#print(f'Correlación Pearson 119: {cor_person_Cumbre_119}')
#print(f'Correlación Pearson 126: {cor_person_Cumbre_126}')
#print(f'Correlación Pearson 245: {cor_person_Cumbre_245}')
#print('....................................................')
#print(f'Correlación Sperman 119: {cor_spearman_Cumbre_119}')
#print(f'Correlación Sperman 126: {cor_spearman_Cumbre_126}')
#print(f'Correlación Sperman 245: {cor_spearman_Cumbre_245}')


#print('================================================================')
#print('Siloe')
#cor_person_Cumbre_119 = temp_Era_pacifico['t2m'].corr(temp_GCM_119['tas'])
#cor_spearman_Cumbre_119 = temp_Era_pacifico['t2m'].corr(temp_GCM_119['tas'], method='spearman')
#cor_person_Cumbre_126 = temp_Era_pacifico['t2m'].corr(temp_GCM_126['tas'])
#cor_spearman_Cumbre_126 = temp_Era_pacifico['t2m'].corr(temp_GCM_126['tas'], method='spearman')
#cor_person_Cumbre_245 = temp_Era_pacifico['t2m'].corr(temp_GCM_245['tas'])
#cor_spearman_Cumbre_245 = temp_Era_pacifico['t2m'].corr(temp_GCM_245['tas'], method='spearman')

#print(f'Correlación Pearson 119: {cor_person_Cumbre_119}')
#print(f'Correlación Pearson 126: {cor_person_Cumbre_126}')
#print(f'Correlación Pearson 245: {cor_person_Cumbre_245}')
#print('.................................................................')
#print(f'Correlación Sperman 119: {cor_spearman_Cumbre_119}')
#print(f'Correlación Sperman 126: {cor_spearman_Cumbre_126}')
#print(f'Correlación Sperman 245: {cor_spearman_Cumbre_245}')



#def k_c (k):
#    c = k - 273.15
#    return c

#temp_GCM_119['tas'] = temp_GCM_119['tas'].apply(k_c)
#temp_GCM_126['tas'] = temp_GCM_126['tas'].apply(k_c)
#temp_GCM_245['tas'] = temp_GCM_245['tas'].apply(k_c)

''' Uniendo columnas por SSPs'''
#temp_GCM_SSP = pd.concat([temp_GCM_119['tas'], temp_GCM_126['tas'], temp_GCM_245['tas']], axis=1)
#temp_GCM_SSP = temp_GCM_SSP.rename(index={ 1: 'tas119', 2: 'tas126', 3: 'tas245'})
#print(temp_GCM_SSP)

''' Exportamos datos SSPs a CSV'''
#temp_GCM_SSP.to_csv('GCM_SSPs_3h.csv', sep=';')
#temp_Era_cumbre.to_csv('Era_cumbre.csv', sep=';')
#temp_Era_pacifico.to_csv('Era_pacifico.csv', sep=';')

#temp_Era_cumbre['t2m'] = temp_Era_cumbre['t2m'].apply(k_c)
#temp_Era_pacifico['t2m'] = temp_Era_pacifico['t2m'].apply(k_c)

''' Plot con Plotly'''
fig = go.Figure()

''' Agregar datos de precipitación'''


''' Agregar datos de temperatura'''
#fig.add_trace(go.Scatter(x = temp_Era_cumbre.index, y = temp_Era_cumbre['t2m'], mode='lines', name='ERA5-Land La Cumbre', line=dict(color='#636EFA')))
#fig.add_trace(go.Scatter(x = temp_Era_pacifico.index, y = temp_Era_pacifico['t2m'], mode='lines', name='ERA5-Land U. Pacífico', line=dict(color='#EF553B')))

#fig.add_trace(go.Scatter(x = temp_GCM_119.index, y = temp_GCM_119['tas'], mode='lines', name='GFDL SSP1-1.9', line=dict(color='#109618')))
#fig.add_trace(go.Scatter(x = temp_GCM_126.index, y = temp_GCM_126['tas'], mode='lines', name='GFDL SSP1-2.6', line=dict(color='#FF9900')))
#fig.add_trace(go.Scatter(x = temp_GCM_245.index, y = temp_GCM_245['tas'], mode='lines', name='GFDL SSP2-4.5', line=dict(color='#DC3912')))
#fig.update_layout(title = 'Temperatura estimada GFDL vs "ERA5-Land"',
#                  title_font_size=22,
#                  legend=dict(title="U. Pacifico: 16 m.s.n.m  La cumbre: 1613 m.s.n.m"),
#                  xaxis_title = 'Tiempo (3h)',
#                  yaxis_title = 'Temperatura °C',
#                  template='seaborn')
#fig.show()

#temp_Era_cumbre.to_csv('ERA_pacifico_3h.csv', sep=';')
#temp_GCM_cumbre.to_csv('GCM119_pacifico_dia.csv', sep=';')
#temp_GCM245_cumbre.to_csv('GCM245_pacifico_dia.csv', sep=';')

#correlacion_GCM_ERA_cumbre = temp_Era_cumbre['t2m'].corr(temp_GCM_119['tas'])
#print(f'Correlación GCM 119 vs ERA5-Land: {correlacion_GCM_ERA_cumbre}')