# -*- coding: utf-8 -*-
"""
Created on Mon Jul 08 12:46:55 2024

Correlacion entre las variables climáticas a modelar

@author: Arturo A. Granada G.
"""

import xarray as xr
import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import plotly.express as px
import plotly.graph_objects as go


r0 = 'Datos/ERA5_Land_T_P/ERA5-Land_2015_2023_ValleDelCauca_3H.nc'
r1 = 'Datos/GCM/GFDL SSP 126/tas_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'
#2 = 'Datos/GCM/GFDL SSP 126/pr_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010130-203412312230_ValleDelCauca.nc'
r3 = 'Datos/GCM/GFDL SSP 126/huss_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'
r4 = 'Datos/GCM/GFDL SSP 126/mrsos_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'
r5 = 'Datos/GCM/GFDL SSP 126/ps_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'
r6 = 'Datos/GCM/GFDL SSP 126/uas_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'
r7 = 'Datos/GCM/GFDL SSP 126/vas_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'

ds0 = xr.open_dataset(r0)
ds1 = xr.open_dataset(r1)
#ds2 = xr.open_dataset(r2)
ds3 = xr.open_dataset(r3)
ds4 = xr.open_dataset(r4)
ds5 = xr.open_dataset(r5)
ds6 = xr.open_dataset(r6)
ds7 = xr.open_dataset(r7)
##ds = xr.merge([ds1, ds3, ds4, ds5, ds6, ds7], compat='override')

''' Selecionamos Pixel de interes del GCM'''
lat = 3.5
lon = 283.1
ds1 = ds1.sel(lon = lon, lat = lat, method='nearest')
ds3 = ds3.sel(lon = lon, lat = lat, method='nearest')
ds4 = ds4.sel(lon = lon, lat = lat, method='nearest')
ds5 = ds5.sel(lon = lon, lat = lat, method='nearest')
ds6 = ds6.sel(lon = lon, lat = lat, method='nearest')
ds7 = ds7.sel(lon = lon, lat = lat, method='nearest')

''' Seleccionamos variables'''
tas = ds1['tas']
##pr = ds2['pr']
huss = ds3['huss']
mrsos = ds4['mrsos']
ps = ds5['ps']
uas = ds6['uas']
vas = ds7['vas']

'''Asignamos el formato de fecha'''
f1 = '2015-01-01 03:00:00'
f2 = '2035-01-01 00:00:00'
fgregoriano = pd.date_range(f1, f2, freq='3h')
fecha = fgregoriano[~((fgregoriano.month == 2) & (fgregoriano.day == 29))]

tas['time'] = fecha
huss['time'] = fecha
mrsos['time'] = fecha
ps['time'] = fecha
uas['time'] = fecha
vas['time'] = fecha

df_tas = tas.to_dataframe().reset_index()
##df_pr = pr.to_dataframe().reset_index()
df_huss = huss.to_dataframe().reset_index().set_index('time', inplace=True)
df_mrsos = mrsos.to_dataframe().reset_index().set_index('time', inplace=True)
df_ps = ps.to_dataframe().reset_index().set_index('time', inplace=True)
df_uas = uas.to_dataframe().reset_index().set_index('time', inplace=True)
df_vas = vas.to_dataframe().reset_index().set_index('time', inplace=True)

df_tas.set_index('time', inplace=True)



f_i = '2015-01-01 03:00:00'
f_f = '2023-12-31 21:00:00'

df_tas = df_tas.loc[f_i:f_f]
#df_huss = df_huss.loc[f_i:f_f]
#df_mrsos = df_mrsos.loc[f_i:f_f]
#df_ps = df_ps.loc[f_i:f_f]
#df_uas = df_uas.loc[f_i:f_f]
#df_vas = df_vas.loc[f_i:f_f]

print(df_tas)

''' Creamos DF'''
#df = ds.to_dataframe().reset_index()#Resetiamos indice como contador 

#df.set_index('time', inplace=True)#Creamos la variable tiempo como indice
#df['time'] = fecha

''' Selecionamos la fecha de interes '''


#df = df.iloc[f_i:f_f]
#print(fecha)
#print(df)

''' Matrix de correlación'''
#features = ['tas', 'huss', 'mrsos', 'ps', 'uas', 'vas']
#fig = px.scatter_matrix(df, dimensions=features)
#fig.update_traces(diagonal_visible=False)
#fig.show()

''' Correlación'''
#correlacion, p_value = pearsonr(df['tas'], df['vas'])
#print(f'Correlación Pearson: {correlacion:.3f}, P-value: {p_value:.3f}')

#correlacion, p_value = spearmanr(df['tas'], df['vas'])
#print(f'Correlación Spearmanr: {correlacion:.3f}, P-value: {p_value:.3f}')






