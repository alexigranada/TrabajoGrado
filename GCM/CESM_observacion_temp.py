# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:29:17 2024

Exploración de Temperatura GCM CESM2-WACCM contra datos observaciones de estaciones meteorologicas

@author: Arturo A. Granada G.
"""

import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

''' 1. Cargar el conjunto de datos CMIP6 (ejemplo: temperatura media diaria) '''
file = 'Datos/GCM/CESM2 WACCM/Tas/tas_day_CESM2-WACCM_ssp245_r3i1p1f1_gn_20150101-20241231_Valle_Cauca.nc'
ds = xr.open_dataset(file)
#longitud_tiempo = len(ds.time)
#ds_recortado = ds.isel(time=slice(0, longitud_tiempo - 2)) #Se realiza corte de los primeros dias de enero del ultimo año
#print(ds_recortado)
print(ds)
''' 2. Cargamos datos de las estaciones'''
r1 = 'Datos/Junio 8/V_Climaticas_LaCumbre_RL_Hora.csv'  #Ruta del archivo
r2 = 'Datos/Junio 8/V_Climaticas_UDelPacifico_Hora.csv'
df_cumbre = pd.read_csv(r1, delimiter=';', index_col='Fecha', parse_dates=['Fecha']) #Cargamos archivo
df_pacifico = pd.read_csv(r2, delimiter=';', index_col='Fecha', parse_dates=['Fecha'])

#print(df_cumbre)
#print(df_pacifico)
''' Creamos el formato de la fecha'''
#estacion_dia['Fecha'] = pd.to_datetime(estacion_dia['Fecha'], format="%Y-%m-%d")
#temp_dia = estacion_dia['ValorMedio']
#time_dia = estacion_dia['Fecha']
#print(time_dia)

'''Transformar la fecha del netCDF'''
ds['time'] = ds.indexes['time'].to_datetimeindex()

''' 3. Cargamos los datos de temperatura del DataSet'''
tas = ds['tas'] - 273.15
tas.attrs['units'] = '°C' #Cambiamos el argumento a °C

f_i = '2018-01-01'
f_f = '2021-12-31'

tas = tas.loc[f_i:f_f]

''' Seleccionamos pixel de interes'''
lat_1 = 4.241 #Latitud del pixel (Mirarlo en en el DF cortado)
lon_1 = 282.5 #Longitud del pixel

lat_2 = 3.298
lon_2 = 283.8

temp_p = tas.sel(lon=lon_1, lat=lat_1, method='nearest') #Seleccionamos pixel con el método 'Valor más cercano'
temp_c = tas.sel(lon=lon_2, lat=lat_2, method='nearest')
df_temp_p = temp_p.to_dataframe()#.reset_index() #Convertimos a DF
df_temp_c = temp_c.to_dataframe()#.reset_index() #Convertimos a DF
#print(df_temp_p)
#print(df_temp_c)

'''Transformar por fecha (Suma, Proemdio)'''
cumbre_dia = df_cumbre.resample('D').mean()
pacifico_dia = df_pacifico.resample('D').mean()

cumbre_dia = cumbre_dia.loc[f_i:f_f]
pacifico_dia = pacifico_dia.loc[f_i:f_f]

'''Transformar a Semana'''
gcm_semana_c = df_temp_c.resample('W').mean()
gcm_semana_p = df_temp_p.resample('W').mean()
cumbre_semana = df_cumbre.resample('W').mean()
pacifico_semana = df_pacifico.resample('W').mean()

cumbre_semana = cumbre_semana.loc[f_i:f_f]
pacifico_semana = pacifico_semana.loc[f_i:f_f]

'''Transformar a Mensual'''
gcm_mes_c = df_temp_c.resample('ME').mean()
gcm_mes_p = df_temp_p.resample('ME').mean()
cumbre_mes = df_cumbre.resample('ME').mean()
pacifico_mes = df_pacifico.resample('ME').mean()

cumbre_mes = cumbre_mes.loc[f_i:f_f]
pacifico_mes = pacifico_mes.loc[f_i:f_f]

''' Plot con Plotly'''
fig = go.Figure()

''' Agregar datos de temperatura'''
fig.add_trace(go.Scatter(x = df_temp_p.index, y = df_temp_p['tas'], mode='lines', name='CESM2 WACCM', line=dict(color='#3366CC')))
fig.add_trace(go.Scatter(x = pacifico_dia.index, y = pacifico_dia['Tmedia'], mode='lines', name='Obs. U. Pacífico', line=dict(color='#DC3912')))
fig.update_layout(title = 'Temperatura SSP2-2.5 CESM2-W vs Observaciones "U. Pacífico"',
                  title_font_size=22,
                  legend=dict(title="Altura: 16 m.s.n.m"),
                  xaxis_title = 'Tiempo (Día)',
                  yaxis_title = 'Temperatura °C',
                  template='seaborn')
fig.show()

'''' Calculamos los valores nulos'''
valores_nulos_c = df_temp_c.isnull().sum()
valores_nulos_c2 = cumbre_dia.isnull().sum()
#print(f'Datos faltantes CESM: {valores_nulos_c}')
#print(f'Datos faltantes Obs: {valores_nulos_c2}')

#title1 = 'CESM_CUMBRE'
#df_temp_c.to_csv(title1, sep=';')#, index=False

#title2 = 'Obs_CUMBRE'
#cumbre_dia.to_csv(title2, sep=';')#, index=False

''' Función para calculo de R2'''
def ecm(x1, x2):
    error2 = (x1-x2)**2
    ecm = np.mean(error2)
    return ecm

error_cuadraticomedio_p_d = ecm(pacifico_dia['Tmedia'], df_temp_p['tas'])
print(f'Error cuadrático medio Pacífico Día: {error_cuadraticomedio_p_d}')

error_cuadraticomedio_c_d = ecm(cumbre_dia['Tmedia'], df_temp_c['tas'])
print(f'Error cuadrático medio Cumbre Día: {error_cuadraticomedio_c_d}')

error_cuadraticomedio_p_s = ecm(pacifico_semana['Tmedia'], gcm_semana_p['tas'])
print(f'Error cuadrático medio Pacífico Semanal: {error_cuadraticomedio_p_s}')

error_cuadraticomedio_c_s = ecm(cumbre_semana['Tmedia'], gcm_semana_c['tas'])
print(f'Error cuadrático medio Cumbre Semanal: {error_cuadraticomedio_c_s}')

error_cuadraticomedio_p_m = ecm(pacifico_mes['Tmedia'], gcm_mes_p['tas'])
print(f'Error cuadrático medio Pacífico Mensual: {error_cuadraticomedio_p_m}')

error_cuadraticomedio_c_m = ecm(cumbre_mes['Tmedia'], gcm_mes_c['tas'])
print(f'Error cuadrático medio Cumbre Mensual: {error_cuadraticomedio_c_m}')

correlacion_CESM_c = cumbre_mes['Tmedia'].corr(gcm_mes_c['tas'])
correlacion_CESM_p = pacifico_mes['Tmedia'].corr(gcm_mes_p['tas'])
print('Correlacion temperatura CESM2 vs Observaciones estación La Cumbre: ', correlacion_CESM_c)
print('Correlacion temperatura CESM2 vs Observaciones estación U. Pacífico: ', correlacion_CESM_p)
#fig.write_image("Temperatura_Dia_Pacifico_CESM_245_OBS.png", width=800, height=500, scale=4)