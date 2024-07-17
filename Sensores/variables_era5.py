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
file = 'Datos/ERA5_Land_T_P/ERA5-Land_2015_2023_ValleDelCauca.nc'
rch = 'Datos/CHIRPS/Dagua.nc'

ds = xr.open_dataset(file)
#ch = xr.open_dataset(rch)
#longitud_tiempo = len(ds.time)
#print(longitud_tiempo)
#ds_recortado = ds.isel(time=slice(0, longitud_tiempo - 2))
#print(ch)

''' 2. Cargamos datos de las estaciones'''
#ruta = 'Datos/Variables Hora/V_Climaticas_LaCumbre_RL_Hora.csv'  #Ruta del archivo
#estacion = pd.read_csv(ruta, delimiter=';') #Cargamos archivo

''' Creamos el formato de la fecha'''
#estacion['Fecha'] = pd.to_datetime(estacion['Fecha'], format="%d/%m/%Y %H:%M")
#temp_dia = estacion['Tmedia']
#time_dia = estacion['Fecha']
#print(estacion)

''' 3. Cargamos los datos de temperatura del DataSet'''
precipitacion = ds['tp']
#precipitacion = ch['prcp']

#tas = ds['t2m'] - 273.15
#u10 = ds['u10']
#v10 = ds['v10']
#presion = ds['sp']
#print(u10)
#tas.attrs['units'] = '°C' #Cambiamos el argumento a °C

''' Seleccionamos pixel de interes'''
#lat_1 = 3.7 #Latitud del pixel (Mirarlo en en el DF cortado)
#lon_1 = -76.6 #Longitud del pixel

#prec = precipitacion.sel(latitude=lat_1, longitude=lon_1, method='nearest')
#df_pt = prec.to_dataframe().reset_index()

def m_mm(m):
    mm = m / 0.01 
    return mm

def pixel_precipitacion (lon_x, lat_y,):
    prec = precipitacion.sel(longitude=lon_x, latitude=lat_y, method='nearest')
    df_pt = prec.to_dataframe().reset_index()
    df_pt['tp'] = df_pt['tp'].apply(m_mm)
    return df_pt 

def pixel_ch (lon_x, lat_y):
    prec = precipitacion.sel(X=lon_x, Y=lat_y, method='nearest')
    df_pt = prec.to_dataframe().reset_index()
    return df_pt


'''La Cumbre ERA'''
df_p1 = pixel_precipitacion(-76.6,3.7)
df_p2 = pixel_precipitacion(-76.5, 3.7)
df_p3 = pixel_precipitacion(-76.6, 3.6)
df_p4 = pixel_precipitacion(-76.5, 3.6)

'''U Pacifico ERA'''
#df_p1 = pixel_precipitacion(3.9, -77.1)
#df_p2 = pixel_precipitacion(3.9, -77)
#df_p3 = pixel_precipitacion(3.9, -76.9)
#df_p4 = pixel_precipitacion(3.8, -77)
#df_p5 = pixel_precipitacion(3.8, -76.9)

'''Farallones ERA'''
#df_p1 = pixel_precipitacion(-76.7, 3.4)
#df_p2 = pixel_precipitacion(-76.6, 3.3)

'''Pacifico CHIRPS'''
#df_p1_1 = pixel_ch(-76.625, 3.425)
#df_p1_2 = pixel_ch(-76.575005, 3.425)
#df_p1_3 = pixel_ch(-76.625, 3.375)
#df_p1_4 = pixel_ch(-76.575005, 3.375)


#df_final = df_p1_1
#df_final['P_1_2'] = df_p1_2['prcp']
#df_final['P_1_3'] = df_p1_3['prcp']
#df_final['P_1_4'] = df_p1_4['prcp']
df_final = df_p1
df_final['P2'] = df_p2['tp']
df_final['P3'] = df_p3['tp']
df_final['P4'] = df_p4['tp']
print(df_final)

#temp = tas.sel(latitude=lat_1, longitude=lon_1, method='nearest') #Seleccionamos pixel con el método 'Valor más cercano'
#df_temp = temp.to_dataframe().reset_index() #Convertimos a DF

''' Plot con Plotly'''
#fig = go.Figure()

''' Agregar datos de temperatura'''
#fig.add_trace(go.Scatter(x = df_temp['time'], y = df_temp['t2m'], mode='lines', name='CESM2'))
#fig.add_trace(go.Scatter(x = time_dia, y = temp_dia, mode='lines', name='Obs Aeropuerto'))
#fig.update_layout(title = 'Temperatura historica CESM2 vs Observaciones',
#                  xaxis_title = 'Año',
#                  yaxis_title = 'Temperatura °C',
#                  template='plotly_white')
#fig.show()

#u_v = u10.sel(latitude=lat_1, longitude=lon_1, method='nearest')
#df_u_v = u_v.to_dataframe().reset_index()

#v_v = v10.sel(latitude=lat_1, longitude=lon_1, method='nearest')
#df_v_v = v_v.to_dataframe().reset_index()
#print(df_v_v)
#patm = presion.sel(latitude=lat_1, longitude=lon_1, method='nearest')
#df_patm = patm.to_dataframe().reset_index()

'''Exportamos a CSV'''
title = f'ERA_Pixel_PT_LaCumbre.csv'
df_final.to_csv(title, sep=';', index=False)


print('Proceso Finalizado')
print('Finalizado sin errores')