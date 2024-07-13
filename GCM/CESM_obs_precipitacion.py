# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:29:17 2024

Exploración de Precipitación GCM CESM2-WACCM contra datos observaciones de estaciones meteorologicas

@author: Arturo A. Granada G.
"""

import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

''' 1. Cargar el conjunto de datos CMIP6 (ejemplo: temperatura media diaria) '''
file = 'Datos/CESM2 WACCM/Pr/pr_day_CESM2-WACCM_ssp245_r3i1p1f1_gn_20150101-20241231_Valle_Cauca.nc'
ds = xr.open_dataset(file)
#longitud_tiempo = len(ds.time)
#ds_recortado = ds.isel(time=slice(0, longitud_tiempo - 2)) #Se realiza corte de los primeros dias de enero del ultimo año
#print(ds_recortado)
#print(ds)
''' 2. Cargamos datos de las estaciones'''
r1 = 'Datos/Junio/V_Climaticas_LaCumbre_RL_Hora.csv'  #Ruta del archivo
r2 = 'Datos/Junio/V_Climaticas_UPacifico_Hora.csv'
df_cumbre   = pd.read_csv(r1, delimiter=';', index_col='Fecha', parse_dates=['Fecha']) #Cargamos archivo
df_pacifico = pd.read_csv(r2, delimiter=',', index_col='Fecha', parse_dates=['Fecha'])

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
pr = ds['pr'] * 86400
pr.attrs['units'] = 'mm/day' #Cambiamos el argumento a °C

f_i = '2018-01-01'
f_f = '2021-12-31'

pr = pr.loc[f_i:f_f]

''' Seleccionamos pixel de interes'''
lat_1 = 4.241 #Latitud del pixel (Mirarlo en en el DF cortado)
lon_1 = 282.5 #Longitud del pixel

lat_2 = 3.298
lon_2 = 283.8

pr_p = pr.sel(lon=lon_1, lat=lat_1, method='nearest') #Seleccionamos pixel con el método 'Valor más cercano'
pr_c = pr.sel(lon=lon_2, lat=lat_2, method='nearest')
df_pr_p = pr_p.to_dataframe()#.reset_index() #Convertimos a DF
df_pr_c = pr_c.to_dataframe()#.reset_index() #Convertimos a DF
#print(df_pr_p)
#print(df_pr_c)

'''Transformar por fecha (Suma, Proemdio)'''
cumbre_dia   = df_cumbre.resample('D').median()
pacifico_dia = df_pacifico.resample('D').median()

cumbre_dia   = cumbre_dia.loc[f_i:f_f]
pacifico_dia = pacifico_dia.loc[f_i:f_f]

print(cumbre_dia)
print(pacifico_dia['PrecipitacionT'])

'''Transformar a Semana'''
gcm_semana_c = df_pr_c.resample('W').median()
gcm_semana_p = df_pr_p.resample('W').median()
cumbre_semana = df_cumbre.resample('W').median()
pacifico_semana = df_pacifico.resample('W').median()

cumbre_semana = cumbre_semana.loc[f_i:f_f]
pacifico_semana = pacifico_semana.loc[f_i:f_f]

'''Transformar a Mensual'''
gcm_mes_c = df_pr_c.resample('ME').median()
gcm_mes_p = df_pr_p.resample('ME').median()
cumbre_mes = df_cumbre.resample('ME').median()
pacifico_mes = df_pacifico.resample('ME').median()

cumbre_mes = cumbre_mes.loc[f_i:f_f]
pacifico_mes = pacifico_mes.loc[f_i:f_f]

''' Plot con Plotly'''
fig = go.Figure()

''' Agregar datos de temperatura'''
fig.add_trace(go.Bar(x=df_pr_p.index, y=df_pr_p['pr'], name='CESM2 WACCM', marker_color='#316395'))
fig.add_trace(go.Bar(x=pacifico_dia.index, y=pacifico_dia['PrecipitacionT'], name='Obs. U. Pacífico', marker_color='#DC3912'))
fig.update_layout(title = 'Precipitación SSP2-2.5 CESM2-W vs Mediciones "U. Pacífico"',
                  title_font_size=22,
                  legend=dict(title="Altura: 16 m.s.n.m"),
                  xaxis_title = 'Tiempo (Día)',
                  yaxis_title = 'Precipitación mm/día',
                  template='seaborn')
fig.show()

'''' Calculamos los valores nulos'''
valores_nulos_c = df_pr_c.isnull().sum()
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

error_cuadraticomedio_p_d = ecm(pacifico_dia['PrecipitacionT'], df_pr_p['pr'])
print(f'Error cuadrático medio Pr Pacífico Día: {error_cuadraticomedio_p_d}')

error_cuadraticomedio_c_d = ecm(cumbre_dia['Precipitacion'], df_pr_c['pr'])
print(f'Error cuadrático medio Pr Cumbre Día: {error_cuadraticomedio_c_d}')

error_cuadraticomedio_p_s = ecm(pacifico_semana['PrecipitacionT'], gcm_semana_p['pr'])
print(f'Error cuadrático medio Pacífico Semanal: {error_cuadraticomedio_p_s}')

error_cuadraticomedio_c_s = ecm(cumbre_semana['Precipitacion'], gcm_semana_c['pr'])
print(f'Error cuadrático medio Cumbre Semanal: {error_cuadraticomedio_c_s}')

error_cuadraticomedio_p_m = ecm(pacifico_mes['PrecipitacionT'], gcm_mes_p['pr'])
print(f'Error cuadrático medio Pacífico Mensual: {error_cuadraticomedio_p_m}')

error_cuadraticomedio_c_m = ecm(cumbre_mes['Precipitacion'], gcm_mes_c['pr'])
print(f'Error cuadrático medio Cumbre Mensual: {error_cuadraticomedio_c_m}')

correlacion_CESM_c = cumbre_semana['Precipitacion'].corr(gcm_semana_c['pr'])
correlacion_CESM_p = pacifico_semana['PrecipitacionT'].corr(gcm_semana_p['pr'])
print('Correlación temperatura CESM2 vs Observaciones estación La Cumbre semana: ', correlacion_CESM_c)
print('Correlación temperatura CESM2 vs Observaciones estación U. Pacífico semana: ', correlacion_CESM_p)
#fig.write_image("Temperatura_Dia_Pacifico_CESM_245_OBS.png", width=800, height=500, scale=4)