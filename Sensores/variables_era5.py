# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:29:17 2024

Exploración de datos ERA5 Land contra datos observaciones de estaciones meteorologicas

@author: Arturo A. Granada G.
"""

import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

''' 1. Cargar el conjunto de datos ERA5 '''
file = 'Datos/ERA5/ERA5-Land_17-22.nc'
ds = xr.open_dataset(file)
#longitud_tiempo = len(ds.time)
#print(longitud_tiempo)
#ds_recortado = ds.isel(time=slice(0, longitud_tiempo - 2))
print(ds)

''' 2. Cargamos datos de las estaciones'''
ruta = 'Datos/Variables Hora/V_Climaticas_LaCumbre_RL_Hora.csv'  #Ruta del archivo
estacion = pd.read_csv(ruta, delimiter=';') #Cargamos archivo

''' Creamos el formato de la fecha'''
estacion['Fecha'] = pd.to_datetime(estacion['Fecha'], format="%d/%m/%Y %H:%M")
temp_dia = estacion['Tmedia']
time_dia = estacion['Fecha']
print(estacion)

''' 3. Cargamos los datos de temperatura del DataSet'''
tas = ds['t2m'] - 273.15
u10 = ds['u10']
v10 = ds['v10']
presion = ds['sp']
#print(u10)
#tas.attrs['units'] = '°C' #Cambiamos el argumento a °C

''' Seleccionamos pixel de interes'''
lat_1 = 3.84 #Latitud del pixel (Mirarlo en en el DF cortado)
lon_1 = -76.98 #Longitud del pixel

temp = tas.sel(latitude=lat_1, longitude=lon_1, method='nearest') #Seleccionamos pixel con el método 'Valor más cercano'

df_temp = temp.to_dataframe().reset_index() #Convertimos a DF

''' Plot con Plotly'''
fig = go.Figure()

''' Agregar datos de temperatura'''
fig.add_trace(go.Scatter(x = df_temp['time'], y = df_temp['t2m'], mode='lines', name='CESM2'))
fig.add_trace(go.Scatter(x = time_dia, y = temp_dia, mode='lines', name='Obs Aeropuerto'))
fig.update_layout(title = 'Temperatura historica CESM2 vs Observaciones',
                  xaxis_title = 'Año',
                  yaxis_title = 'Temperatura °C',
                  template='plotly_white')
#fig.show()

u_v = u10.sel(latitude=lat_1, longitude=lon_1, method='nearest')
df_u_v = u_v.to_dataframe().reset_index()

v_v = v10.sel(latitude=lat_1, longitude=lon_1, method='nearest')
df_v_v = v_v.to_dataframe().reset_index()
#print(df_v_v)
patm = presion.sel(latitude=lat_1, longitude=lon_1, method='nearest')
df_patm = patm.to_dataframe().reset_index()

'''Exportamos a CSV'''
title = f'ERA5_Patm_UP.csv'
df_patm.to_csv(title, sep=';', index=False)
print('Proceso Finalizado')
print('Finalizado sin errores')