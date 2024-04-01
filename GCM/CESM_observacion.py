# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:29:17 2024

Exploración de datos GCM CESM2-WACCM contra datos observaciones de estaciones meteorologicas

@author: Arturo A. Granada G.
"""

import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

''' 1. Cargar el conjunto de datos CMIP6 (ejemplo: temperatura media diaria) '''
file = 'Datos/GCM/CESM2 WACCM/Temperature/tas_day_CESM2-WACCM_historical_r2i1p1f1_gn_20000101-20150101_Valle_Cauca.nc'
ds = xr.open_dataset(file)
longitud_tiempo = len(ds.time)
ds_recortado = ds.isel(time=slice(0, longitud_tiempo - 2))
print(ds_recortado)

''' 2. Cargamos datos de las estaciones'''
ruta_dia = 'Datos/Estaciones/IDEAM/Estaciones Dagua/Temperatura dia/Temperatura_dia_AEROPUERTO BUENAVENTUR [53115010].csv'  #Ruta del archivo
estacion_dia = pd.read_csv(ruta_dia, delimiter=';') #Cargamos archivo

''' Creamos el formato de la fecha'''
estacion_dia['Fecha'] = pd.to_datetime(estacion_dia['Fecha'], format="%Y-%m-%d")
temp_dia = estacion_dia['ValorMedio']
time_dia = estacion_dia['Fecha']
print(time_dia)

''' 3. Cargamos los datos de temperatura del DataSet'''
tas = ds_recortado['tas'] - 273.15
tas.attrs['units'] = '°C' #Cambiamos el argumento a °C

''' Seleccionamos pixel de interes'''
lat_1 = 4.241 #Latitud del pixel (Mirarlo en en el DF cortado)
lon_1 = 282.5 #Longitud del pixel

temp_1 = tas.sel(lat=lat_1, lon=lon_1, method='nearest') #Seleccionamos pixel con el método 'Valor más cercano'

df_temp = temp_1.to_dataframe().reset_index() #Convertimos a DF

''' Plot con Plotly'''
fig = go.Figure()
''' Agregar datos de temperatura'''
fig.add_trace(go.Scatter(x = df_temp['time'], y = df_temp['tas'], mode='lines', name='CESM2'))
fig.add_trace(go.Scatter(x = time_dia, y = temp_dia, mode='lines', name='Obs Aeropuerto'))
fig.update_layout(title = 'Temperatura historica CESM2 vs Observaciones',
                  xaxis_title = 'Año',
                  yaxis_title = 'Temperatura °C',
                  template='plotly_white')
fig.show()