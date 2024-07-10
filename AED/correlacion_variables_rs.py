# -*- coding: utf-8 -*-
"""
Created on Mon Jul 08 12:46:55 2024

Correlacion entre las variables climáticas Radiación solar con las variables a modelar

@author: Arturo A. Granada G.
"""

import xarray as xr
import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import plotly.express as px
import plotly.graph_objects as go


r0 = 'Datos/ERA5_Land_T_P/ERA5-Land_2015_2023_ValleDelCauca_3H.nc'
r1 = 'Datos/GCM/GFDL SSP 126/rlds_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010130-203412312230_ValleDelCauca.nc'
r3 = 'Datos/GCM/GFDL SSP 126/rlus_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010130-203412312230_ValleDelCauca.nc'
r4 = 'Datos/GCM/GFDL SSP 126/rsds_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010130-203412312230_ValleDelCauca.nc'
r5 = 'Datos/GCM/GFDL SSP 126/rsus_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010130-203412312230_ValleDelCauca.nc'
#r6 = 'Datos/GCM/GFDL SSP 126/uas_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'
#r7 = 'Datos/GCM/GFDL SSP 126/vas_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'
#2 = 'Datos/GCM/GFDL SSP 126/pr_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010130-203412312230_ValleDelCauca.nc'

ds0 = xr.open_dataset(r0)
ds1 = xr.open_dataset(r1)
ds3 = xr.open_dataset(r3)
ds4 = xr.open_dataset(r4)
ds5 = xr.open_dataset(r5)
#ds6 = xr.open_dataset(r6)
#ds7 = xr.open_dataset(r7)
#ds2 = xr.open_dataset(r2)

''' Selecionamos Pixel de interes del GCM'''
lat = 3.5
lon = 283.1
ds1 = ds1.sel(lon = lon, lat = lat, method='nearest')
ds3 = ds3.sel(lon = lon, lat = lat, method='nearest')
ds4 = ds4.sel(lon = lon, lat = lat, method='nearest')
ds5 = ds5.sel(lon = lon, lat = lat, method='nearest')

''' Seleccionamos el pixel para cada una de las estaciones'''
lon_pacifico, lat_pacifico = -76.5647 , 3.8480
lon_cumbre, lat_cumbre = -76.5674 , 3.6451
lon_farallones, lat_farallones = -76.6513 , 3.4158
lon_univalle, lat_univalle = -76.5338 , 3.377
lon_aBonilla, lat_aBonilla = -76.3822 , 3.5327
lon_diana, lat_diana = -76.1855 , 3.3138

pacifico = ds0.sel(longitude = lon_pacifico, latitude = lat_pacifico, method='nearest')
cumbre = ds0.sel(longitude = lon_cumbre, latitude= lat_cumbre, method='nearest')
farallones = ds0.sel(longitude = lon_farallones, latitude = lat_farallones, method='nearest')
univalle = ds0.sel(longitude = lon_univalle, latitude = lat_univalle, method='nearest')
aBonilla = ds0.sel(longitude = lon_aBonilla, latitude = lat_aBonilla, method='nearest')
diana = ds0.sel(longitude = lon_diana, latitude = lat_diana, method='nearest')

''' Seleccionamos variables GCM'''
rlds = ds1['rlds']
rlus = ds3['rlus']
rsds = ds4['rsds']
rsus = ds5['rsus']

''' Seleccionamos variables ERA5-Land'''
pacifico_t2m = pacifico['t2m']
cumbre_t2m = cumbre['t2m']
farallones_t2m = farallones['t2m']
univalle_t2m = univalle['t2m']
aBonilla_t2m = aBonilla['t2m']
diana_t2m = diana['t2m']

'''Asignamos el formato de fecha para GCM'''
f1 = '2015-01-01 03:00:00'
f2 = '2035-01-01 00:00:00'
fgregoriano = pd.date_range(f1, f2, freq='3h')
fecha = fgregoriano[~((fgregoriano.month == 2) & (fgregoriano.day == 29))]

rlds['time'] = fecha
rlus['time'] = fecha
rsds['time'] = fecha
rsus['time'] = fecha

''' Asignamos la Fecha para ERA5-Land sin días bisiestos'''
pacifico_t2m = pacifico_t2m.loc['2015-01-01 03:00':'2023-12-31 21:00']
cumbre_t2m = cumbre_t2m.loc['2015-01-01 03:00':'2023-12-31 21:00']
farallones_t2m = farallones_t2m.loc['2015-01-01 03:00':'2023-12-31 21:00']
univalle_t2m = univalle_t2m.loc['2015-01-01 03:00':'2023-12-31 21:00']
aBonilla_t2m = aBonilla_t2m.loc['2015-01-01 03:00':'2023-12-31 21:00']
diana_t2m = diana_t2m.loc['2015-01-01 03:00':'2023-12-31 21:00']

pacifico_t2m_era = pacifico_t2m.loc[~((pacifico_t2m['time'].dt.month == 2) & (pacifico_t2m['time'].dt.day == 29))]
cumbre_t2m_era = cumbre_t2m.loc[~((cumbre_t2m['time'].dt.month == 2) & (cumbre_t2m['time'].dt.day == 29))]
farallones_t2m_era = farallones_t2m.loc[~((farallones_t2m['time'].dt.month == 2) & (farallones_t2m['time'].dt.day == 29))]
univalle_t2m_era = univalle_t2m.loc[~((univalle_t2m['time'].dt.month == 2) & (univalle_t2m['time'].dt.day == 29))]
aBonilla_t2m_era = aBonilla_t2m.loc[~((aBonilla_t2m['time'].dt.month == 2) & (aBonilla_t2m['time'].dt.day == 29))]
diana_t2m_era = diana_t2m.loc[~((diana_t2m['time'].dt.month == 2) & (diana_t2m['time'].dt.day == 29))]

''' Convertimos a DF'''
df_rlds = rlds.to_dataframe().reset_index()
df_rlus = rlus.to_dataframe().reset_index()
df_rsds = rsds.to_dataframe().reset_index()
df_rsus = rsus.to_dataframe().reset_index()

df_pacifico = pacifico_t2m_era.to_dataframe().reset_index()
df_cumbre = cumbre_t2m_era.to_dataframe().reset_index()
df_farallones = farallones_t2m_era.to_dataframe().reset_index()
df_univalle = univalle_t2m_era.to_dataframe().reset_index()
df_aBonilla = aBonilla_t2m_era.to_dataframe().reset_index()
df_diana = diana_t2m_era.to_dataframe().reset_index()

''' Creamos la fecha como indice'''
df_rlds.set_index('time', inplace=True)
df_rlus.set_index('time', inplace=True)
df_rsds.set_index('time', inplace=True)
df_rsus.set_index('time', inplace=True)

df_pacifico.set_index('time', inplace=True)
df_cumbre.set_index('time', inplace=True)
df_farallones.set_index('time', inplace=True)
df_univalle.set_index('time', inplace=True)
df_aBonilla.set_index('time', inplace=True)
df_diana.set_index('time', inplace=True)

''' Seleccionamos el rango de fecha de interes'''
f_i = '2015-01-01 03:00:00'
f_f = '2023-12-31 21:00:00'

df_rlds = df_rlds.loc[f_i:f_f]
df_rlus = df_rlus.loc[f_i:f_f]
df_rsds = df_rsds.loc[f_i:f_f]
df_rsus = df_rsus.loc[f_i:f_f]

#print(df_rlds)
#print(df_pacifico)

''' Correlación'''
print('Correlación rlds')
correlacion, p_value = spearmanr(df_pacifico['t2m'], df_rlds['rlds'])
print(f'Correlación Spearmanr: {correlacion:.3f}, P-value: {p_value:.3f}')

correlacion, p_value = pearsonr(df_pacifico['t2m'], df_rlds['rlds'])
print(f'Correlación Pearson: {correlacion:.3f}, P-value: {p_value:.3f}')

print('Correlación rlus')
correlacion, p_value = spearmanr(df_pacifico['t2m'], df_rlus['rlus'])
print(f'Correlación Spearmanr: {correlacion:.3f}, P-value: {p_value:.3f}')

correlacion, p_value = pearsonr(df_pacifico['t2m'], df_rlus['rlus'])
print(f'Correlación Pearson: {correlacion:.3f}, P-value: {p_value:.3f}')

print('Correlación rsds')
correlacion, p_value = spearmanr(df_pacifico['t2m'], df_rsds['rsds'])
print(f'Correlación Spearmanr: {correlacion:.3f}, P-value: {p_value:.3f}')

correlacion, p_value = pearsonr(df_pacifico['t2m'], df_rsds['rsds'])
print(f'Correlación Pearson: {correlacion:.3f}, P-value: {p_value:.3f}')

print('Correlación rsus')
correlacion, p_value = spearmanr(df_pacifico['t2m'], df_rsus['rsus'])
print(f'Correlación Spearmanr: {correlacion:.3f}, P-value: {p_value:.3f}')

correlacion, p_value = pearsonr(df_pacifico['t2m'], df_rsus['rsus'])
print(f'Correlación Pearson: {correlacion:.3f}, P-value: {p_value:.3f}')