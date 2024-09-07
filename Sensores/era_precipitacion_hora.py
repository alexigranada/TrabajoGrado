# -*- coding: utf-8 -*-
"""
Created on Wed July 30 18:04:05 2024

Los datos de precipitación de ERA5-Land son por hora acumulada a día
Creamos un scrip para restar la hora anterior y crear la precipitación por hora individual

@author: Arturo A. Granada G.
"""

import xarray as xr
import plotly.graph_objects as GO

r1 = 'Datos/ERA5_Land_T_P/ERA5-Land_2015_2023_ValleDelCauca.nc'
ds1 = xr.open_dataset(r1)

'''La hora inicial 01:00 no se le realiza la resta '''
ds1['precipitation_hourly'] = ds1['tp'].diff(dim='time')

''' Mantén el valor de precipitación en la primera hora de cada día '''
is_first_hour = ds1['time'].dt.hour == 1
ds1['precipitation_hourly'] = xr.where(is_first_hour, ds1['tp'], ds1['precipitation_hourly'])

''' Si deseas guardar el nuevo dataset con los valores de precipitación por hora '''
print(ds1)
ds1.to_netcdf('ERA5-Land_2015_2023_ValleDelCauca_Hora_individual.nc')

'''Seleccionamos las variables y periodo de estudio'''
f_i = '2015-01-01 01:00:00'
f_f = '2023-12-31 23:00:00'

p_ERA = ds1['precipitation_hourly'] / 0.01
p_ERA.attrs['units'] = 'mm/day' 
p_ERA = p_ERA.loc[f_i:f_f]
''' Seleccionamos pixel de interes'''
lon_ERA_farallones = -76.6513
lat_ERA_farallones = 3.4158

lon_ERA_arpto = -76.3822
lat_ERA_arpto = 3.5327

lon_ERA_diana = -76.1855
lat_ERA_diana = 3.3138

lon_ERA_cumbre = -76.5647
lat_ERA_cumbre = 3.6451

lon_ERA_siloe = -76.5605
lat_ERA_siloe = 3.4252

lon_ERA_univalle = -76.5338
lat_ERA_univalle = 3.3777

lon_ERA_pacifico = -76.9869
lat_ERA_pacifico = 3.8480 

p_ERA_arpto = p_ERA.sel(longitude=lon_ERA_pacifico, latitude=lat_ERA_pacifico, method='nearest')

pre_Era_arpto = p_ERA_arpto.to_dataframe().reset_index()

pre_Era_arpto.to_csv('Prec_ERA_Unipacifico_Hora_simple.csv', sep=';', index=True)
#df_final.to_csv(title, sep=';', index=False)

''' Extraer la hora de la columna 'Fecha' '''
pre_Era_arpto['Hora'] = pre_Era_arpto['time'].dt.hour

''' Agrupar por la hora y sumar los valores '''
Era_hora_arpto = pre_Era_arpto.groupby('Hora')['precipitation_hourly'].mean().reset_index()

fig = GO.Figure()
fig.add_trace(GO.Bar(x=Era_hora_arpto['Hora'], y=Era_hora_arpto['precipitation_hourly'], name='ERA5-Land'))
fig.show()