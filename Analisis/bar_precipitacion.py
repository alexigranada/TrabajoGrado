# -*- coding: utf-8 -*-
"""
Created on Wed July 30 13:06:57 2024

Exploración de datos GCM contra datos ERA5-Land de precipitación en cajas de bloxplot

@author: Arturo A. Granada G.
"""

import xarray as xr
import pandas as PD
import numpy as NP
import plotly.express as PX
import plotly.graph_objects as GO
import plotly.figure_factory as ff
from plotly.subplots import make_subplots

r1 = 'Datos/GCM/pr_3hr_GFDL-ESM4_ssp119_r1i1p1f1_gr1_201501010130-203412312230_ValleDelCauca.nc'
r2 = 'Datos/GCM/pr_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010130-203412312230_ValleDelCauca.nc'
r3 = 'Datos/GCM/pr_3hr_GFDL-ESM4_ssp245_r1i1p1f1_gr1_201501010130-203412312230_ValleDelCauca.nc'
r4 = 'Datos/ERA5_Land_T_P/ERA5-Land_2015_2023_ValleDelCauca_Hora.nc'

r5 = 'Datos/Precipitacion_Arpto.csv'
r6 = 'Datos/Precipitacion_Farallones.csv'
r7 = 'Datos/Precipitacion_Cumbre.csv'
r8 = 'Datos/Precipitacion_Diana.csv'
r9 = 'Datos/Precipitacion_Siloe.csv'
r10 = 'Datos/Precipitacion_Univalle.csv'
r11 = 'Datos/Precipitacion_Unipacifico.csv'

r12 = 'Datos/V_Climaticas_Arpto_Medicion_ERA.csv'
r13 = 'Datos/Farallones_5.csv'
r14 = 'Datos/Cumbre_5.csv'
r15 = 'Datos/Diana_5.csv'
r16 = 'Datos/Siloe_5.csv'
r17 = 'Datos/UP_5.csv'
r18 = 'Datos/UV_5.csv'

ds1 = xr.open_dataset(r1)
ds2 = xr.open_dataset(r2)
ds3 = xr.open_dataset(r3)
ds4 = xr.open_dataset(r4)

df5 = PD.read_csv(r5, sep=',')
df5['Fecha'] = PD.to_datetime(df5['Fecha'], format='%Y-%m-%d %H:%M:%S')
#df5.set_index('Fecha', inplace=True)
#df5 = df5.resample('ME').sum().reset_index()

df6 = PD.read_csv(r6, sep=',')
df6['Fecha'] = PD.to_datetime(df6['Fecha'], format='%Y-%m-%d %H:%M:%S')
#df6.set_index('Fecha', inplace=True)
#df6 = df6.resample('ME').sum().reset_index()

df7 = PD.read_csv(r7, sep=',')
df7['Fecha'] = PD.to_datetime(df7['Fecha'], format='%Y-%m-%d %H:%M:%S')
#df7.set_index('Fecha', inplace=True)
#df7 = df7.resample('ME').sum().reset_index()

df8 = PD.read_csv(r8, sep=',')
df8['Fecha'] = PD.to_datetime(df8['Fecha'], format='%Y-%m-%d %H:%M:%S')
#df8.set_index('Fecha', inplace=True)
#df8 = df8.resample('ME').sum().reset_index()

df9 = PD.read_csv(r9, sep=',')
df9['Fecha'] = PD.to_datetime(df9['Fecha'], format='%Y-%m-%d %H:%M:%S')
#df9.set_index('Fecha', inplace=True)
#df9 = df9.resample('ME').sum().reset_index()

df10 = PD.read_csv(r10, sep=',')
df10['Fecha'] = PD.to_datetime(df10['Fecha'], format='%Y-%m-%d %H:%M:%S')
#df10.set_index('Fecha', inplace=True)
#df10 = df10.resample('ME').sum().reset_index()

df11 = PD.read_csv(r11, sep=',')
df11['Fecha'] = PD.to_datetime(df11['Fecha'], format='%Y-%m-%d %H:%M:%S')
#df11.set_index('Fecha', inplace=True)
#df11 = df11.resample('ME').sum().reset_index()

df12 = PD.read_csv(r12, sep=',')
df12['Fecha'] = PD.to_datetime(df12['Fecha'], format='%Y-%m-%d %H:%M:%S')

df13 = PD.read_csv(r13, sep=',')
df13['Fecha'] = PD.to_datetime(df13['Fecha'], format='%Y-%m-%d %H:%M:%S')

df14 = PD.read_csv(r14, sep=';')
df14['Fecha'] = PD.to_datetime(df14['Fecha'], format='%Y-%m-%d %H:%M:%S')

df15 = PD.read_csv(r15, sep=';')
df15['Fecha'] = PD.to_datetime(df15['Fecha'], format='%Y-%m-%d %H:%M:%S')

df16 = PD.read_csv(r16, sep=';')
df16['Fecha'] = PD.to_datetime(df16['Fecha'], format='%Y-%m-%d %H:%M:%S')

df17 = PD.read_csv(r17, sep=';')
df17['Fecha'] = PD.to_datetime(df17['Fecha'], format='%Y-%m-%d %H:%M:%S')

df18 = PD.read_csv(r18, sep=';')
df18['Fecha'] = PD.to_datetime(df18['Fecha'], format='%Y-%m-%d %H:%M:%S')

'''Seleccionamos las variables y periodo de estudio'''
f_i = '2015-01-01 01:00:00'
f_f = '2023-12-31 23:00:00'

p_119 = ds1['pr'] * 86400
p_126 = ds2['pr'] * 86400
p_245 = ds3['pr'] * 86400
p_ERA = ds4['precipitation_hourly'] / 0.01
t_ERA = ds4['t2m'] - 273.15

p_119.attrs['units'] = 'mm/day'
p_126.attrs['units'] = 'mm/day'
p_245.attrs['units'] = 'mm/day'
p_ERA.attrs['units'] = 'mm/day'

p_119 = p_119.loc[f_i:f_f]
p_126 = p_126.loc[f_i:f_f]
p_245 = p_245.loc[f_i:f_f]
#p_ERA = p_ERA.loc[f_i:f_f]
#p_ERA = p_ERA.loc[~((p_ERA['time'].dt.month == 2) & (p_ERA['time'].dt.day == 29))]

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

lon_ERA_pacifico = -76.9869
lat_ERA_pacifico = 3.8480 

p_GCM_119 = p_119.sel(lon=lon_GCM, lat=lat_GCM, method='nearest')
p_GCM_126 = p_126.sel(lon=lon_GCM, lat=lat_GCM, method='nearest')
p_GCM_245 = p_245.sel(lon=lon_GCM, lat=lat_GCM, method='nearest')
p_ERA_arpto = p_ERA.sel(longitude=lon_ERA_arpto, latitude=lat_ERA_arpto, method='nearest')
p_ERA_farallones = p_ERA.sel(longitude=lon_ERA_farallones, latitude=lat_ERA_farallones, method='nearest')
p_ERA_cumbre = p_ERA.sel(longitude=lon_ERA_cumbre, latitude=lat_ERA_cumbre, method='nearest')
p_ERA_diana = p_ERA.sel(longitude=lon_ERA_diana, latitude=lat_ERA_diana, method='nearest')
p_ERA_siloe = p_ERA.sel(longitude=lon_ERA_siloe, latitude=lat_ERA_siloe, method='nearest')
p_ERA_univalle = p_ERA.sel(longitude=lon_ERA_univalle, latitude=lat_ERA_univalle, method='nearest')
p_ERA_pacifico = p_ERA.sel(longitude=lon_ERA_pacifico, latitude=lat_ERA_pacifico, method='nearest')

t_ERA_arpto = t_ERA.sel(longitude=lon_ERA_arpto, latitude=lat_ERA_arpto, method='nearest')
t_ERA_farallones = t_ERA.sel(longitude=lon_ERA_farallones, latitude=lat_ERA_farallones, method='nearest')
t_ERA_cumbre = t_ERA.sel(longitude=lon_ERA_cumbre, latitude=lat_ERA_cumbre, method='nearest')
t_ERA_diana = t_ERA.sel(longitude=lon_ERA_diana, latitude=lat_ERA_diana, method='nearest')
t_ERA_siloe = t_ERA.sel(longitude=lon_ERA_siloe, latitude=lat_ERA_siloe, method='nearest')
t_ERA_univalle = t_ERA.sel(longitude=lon_ERA_univalle, latitude=lat_ERA_univalle, method='nearest')
t_ERA_pacifico = t_ERA.sel(longitude=lon_ERA_pacifico, latitude=lat_ERA_pacifico, method='nearest')

pre_GCM_119 = p_GCM_119.to_dataframe().reset_index() 
pre_GCM_126 = p_GCM_126.to_dataframe().reset_index()
pre_GCM_245 = p_GCM_245.to_dataframe().reset_index()

pre_Era_arpto = p_ERA_arpto.to_dataframe().reset_index()
pre_Era_farallones = p_ERA_farallones.to_dataframe().reset_index()
pre_Era_cumbre = p_ERA_cumbre.to_dataframe().reset_index()
pre_Era_diana = p_ERA_diana.to_dataframe().reset_index()
pre_Era_siloe = p_ERA_siloe.to_dataframe().reset_index()
pre_Era_univalle = p_ERA_univalle.to_dataframe().reset_index() 
pre_Era_pacifico = p_ERA_pacifico.to_dataframe().reset_index()

tem_Era_arpto = t_ERA_arpto.to_dataframe().reset_index()
tem_Era_farallones = t_ERA_farallones.to_dataframe().reset_index()
tem_Era_cumbre = t_ERA_cumbre.to_dataframe().reset_index()
tem_Era_diana = t_ERA_diana.to_dataframe().reset_index()
tem_Era_siloe = t_ERA_siloe.to_dataframe().reset_index()
tem_Era_univalle = t_ERA_univalle.to_dataframe().reset_index() 
tem_Era_pacifico = t_ERA_pacifico.to_dataframe().reset_index()

correlacion = tem_Era_arpto['t2m'].corr(df12['Tmedia'])
print(f'Correlacion: {correlacion}')

pre_GCM_119['time'] = PD.to_datetime(pre_GCM_119['time'], format='%Y-%m-%d %H:%M:%S')
pre_GCM_126['time'] = PD.to_datetime(pre_GCM_126['time'], format='%Y-%m-%d %H:%M:%S')
pre_GCM_245['time'] = PD.to_datetime(pre_GCM_245['time'], format='%Y-%m-%d %H:%M:%S')

''' Crea una columna para identificar si es la primera hora del día (01:00)'''
#pre_Era_arpto['Es_primera_hora'] = pre_Era_arpto['time'].dt.hour == 1

''' Calcula la diferencia entre las horas consecutivas '''
#pre_Era_arpto['precipitacion_hora'] = pre_Era_arpto['tp'].diff()

''' Reemplaza los valores de la primera hora de cada día con NaN o 0, según prefieras '''
#pre_Era_arpto.loc[pre_Era_arpto['Es_primera_hora'], 'precipitacion_hora'] = pre_Era_arpto['tp']


''' Extraer la hora de la columna 'Fecha' (month-day-hour)''' 
pre_GCM_245['Hora'] = pre_GCM_245['time'].dt.hour

pre_Era_arpto['Hora'] = pre_Era_arpto['time'].dt.hour
pre_Era_farallones['Hora'] = pre_Era_farallones['time'].dt.hour
pre_Era_cumbre['Hora'] = pre_Era_cumbre['time'].dt.hour
pre_Era_diana['Hora'] = pre_Era_diana['time'].dt.hour
pre_Era_siloe['Hora'] = pre_Era_siloe['time'].dt.hour
pre_Era_univalle['Hora'] = pre_Era_univalle['time'].dt.hour
pre_Era_pacifico['Hora'] = pre_Era_pacifico['time'].dt.hour

tem_Era_arpto['Hora'] = tem_Era_arpto['time'].dt.hour
tem_Era_farallones['Hora'] = tem_Era_farallones['time'].dt.hour
tem_Era_cumbre['Hora'] = tem_Era_cumbre['time'].dt.hour
tem_Era_diana['Hora'] = tem_Era_diana['time'].dt.hour
tem_Era_siloe['Hora'] = tem_Era_siloe['time'].dt.hour
tem_Era_univalle['Hora'] = tem_Era_univalle['time'].dt.hour
tem_Era_pacifico['Hora'] = tem_Era_pacifico['time'].dt.hour

df5['Hora'] = df5['Fecha'].dt.hour
df6['Hora'] = df6['Fecha'].dt.hour
df7['Hora'] = df7['Fecha'].dt.hour
df8['Hora'] = df8['Fecha'].dt.hour
df9['Hora'] = df9['Fecha'].dt.hour
df10['Hora'] = df10['Fecha'].dt.hour
df11['Hora'] = df11['Fecha'].dt.hour

df12['Hora'] = df12['Fecha'].dt.hour
df13['Hora'] = df13['Fecha'].dt.hour
df14['Hora'] = df14['Fecha'].dt.hour
df15['Hora'] = df15['Fecha'].dt.hour
df16['Hora'] = df16['Fecha'].dt.hour
df17['Hora'] = df17['Fecha'].dt.hour
df18['Hora'] = df18['Fecha'].dt.hour
#print(pre_Era_arpto)

''' Agrupar por la hora y sumar los valores '''
#GCM_hora_245 = pre_GCM_245.groupby('Hora')['pr'].sum().reset_index()

Era_hora_arpto = pre_Era_arpto.groupby('Hora')['precipitation_hourly'].mean().reset_index()
Era_hora_farallones = pre_Era_farallones.groupby('Hora')['precipitation_hourly'].mean().reset_index()
Era_hora_cumbre = pre_Era_cumbre.groupby('Hora')['precipitation_hourly'].mean().reset_index()
Era_hora_diana = pre_Era_diana.groupby('Hora')['precipitation_hourly'].mean().reset_index()
Era_hora_siloe = pre_Era_siloe.groupby('Hora')['precipitation_hourly'].mean().reset_index()
Era_hora_univalle = pre_Era_univalle.groupby('Hora')['precipitation_hourly'].mean().reset_index()
Era_hora_pacifico = pre_Era_pacifico.groupby('Hora')['precipitation_hourly'].mean().reset_index()

Era_hora_arpto_t = tem_Era_arpto.groupby('Hora')['t2m'].mean().reset_index()
Era_hora_farallones_t = tem_Era_farallones.groupby('Hora')['t2m'].mean().reset_index()
Era_hora_cumbre_t = tem_Era_cumbre.groupby('Hora')['t2m'].mean().reset_index()
Era_hora_diana_t = tem_Era_diana.groupby('Hora')['t2m'].mean().reset_index()
Era_hora_siloe_t = tem_Era_siloe.groupby('Hora')['t2m'].mean().reset_index()
Era_hora_univalle_t = tem_Era_univalle.groupby('Hora')['t2m'].mean().reset_index()
Era_hora_pacifico_t = tem_Era_pacifico.groupby('Hora')['t2m'].mean().reset_index()

Est_hora_arpto = df5.groupby('Hora')['Ptotal'].mean().reset_index()
Est_hora_farallones = df6.groupby('Hora')['Ptotal'].mean().reset_index()
Est_hora_cumbre = df7.groupby('Hora')['Ptotal'].mean().reset_index()
Est_hora_diana = df8.groupby('Hora')['Ptotal'].mean().reset_index()
Est_hora_siloe = df9.groupby('Hora')['Ptotal'].mean().reset_index()
Est_hora_univalle = df10.groupby('Hora')['Ptotal'].mean().reset_index()
Est_hora_pacifico = df11.groupby('Hora')['Ptotal'].mean().reset_index()

Est_hora_arpto_t = df12.groupby('Hora')['Tmedia'].mean().reset_index()
Est_hora_farallones_t = df13.groupby('Hora')['Tmedia'].mean().reset_index()
Est_hora_cumbre_t = df14.groupby('Hora')['Tmedia'].mean().reset_index()
Est_hora_diana_t = df15.groupby('Hora')['Tmedia'].mean().reset_index()
Est_hora_siloe_t = df16.groupby('Hora')['Tmedia'].mean().reset_index()
Est_hora_univalle_t = df17.groupby('Hora')['Tmedia'].mean().reset_index()
Est_hora_pacifico_t = df18.groupby('Hora')['Tmedia'].mean().reset_index()

#print(Era_hora_arpto)
#print(Est_hora_arpto)

fig = make_subplots(specs=[[{"secondary_y": True}]])
#fig = GO.Figure()
#fig.add_trace(GO.Bar(x=pre_Era_arpto['time'], y=pre_Era_arpto['precipitacion_hora'], name='Hora'))
#fig.add_trace(GO.Bar(x=pre_Era_arpto['time'], y=pre_Era_arpto['tp'], name='Acumulada'))
#fig.show()


#fig = GO.Figure()
#fig.add_trace(GO.Bar(x=GCM_hora_245['Hora'], y=GCM_hora_245['pr'], name='GFDL-ESM4'))
fig.add_trace(GO.Bar(x=Era_hora_arpto['Hora'], y=Era_hora_arpto['precipitation_hourly'], name='ERA5-Land', marker_color='#3366CC', yaxis='y1')) #
fig.add_trace(GO.Bar(x=Est_hora_arpto['Hora'], y=Est_hora_arpto['Ptotal'], name='Observación', marker_color='#DC3912', yaxis='y1')) #

fig.add_trace(GO.Scatter(x=Era_hora_arpto_t['Hora'], y=Era_hora_arpto_t['t2m'], mode='lines+markers', name='ERA5-Land', marker_color='#00A08B', yaxis='y2'))#Rojo EF553B
fig.add_trace(GO.Scatter(x=Est_hora_arpto_t['Hora'], y=Est_hora_arpto_t['Tmedia'], mode='lines+markers', name='Observación', marker_color='#1616A7', yaxis='y2'))#Verde 00CC96

title = f'Precipitación y temperatura promedio por hora (2015-2023)'
fig.update_layout(title = title,
                  title_font_size=22,
                  xaxis = dict(title='Tiempo (Hora)'),
                  yaxis = dict(title='Precipitación (mm)'),
                  yaxis2 = dict(title='Temperatura (°C)', side='right'),
                  template = 'seaborn',
                  title_x = 0.5)
#fig.write_image('Precipitacion total ERA5-Land.png', width=800, height=500, scale=4)
fig.show()

#fig2 = GO.Figure()
#fig2.add_trace(GO.Box(x=pre_Era_arpto['Hora'], y=pre_Era_arpto['precipitation_hourly'], boxmean=True, name='ERA5-Land', marker_color='#00CC96'))
#fig2.add_trace(GO.Box(x=df5['Hora'], y=df5['Ptotal'], boxmean=True, name='Observación', marker_color='#636EFA'))
#fig2.show()
#fig2 = GO.Figure()
#fig2.add_trace(GO.Bar(x=pre_GCM_119['time'], y=pre_GCM_119['pr'], name='SSP1 - 1.9'))
#fig2
#fig2.show()

#hist_data = [ pre_GCM_245['pr']] #pre_Era_arpto['precipitation_hourly'],, df5['Ptotal']
#group_labels = ['GFDL-ESM4'] #'ERA5-Land',, 'Observación'
#colors = ['#636EFA', '#EF553B', '#00CC96', '#7FA6EE', '#B8F7D4']

#fig = ff.create_distplot(hist_data, group_labels, bin_size=0, colors=colors, curve_type='normal')
#fig.update_layout(
#    title='Distribución temperatura Estación "Arpto"',
#    title_font_size = 22,
#    yaxis = dict(title='Frecuencia'),
#    xaxis = dict(title='Temperatura (°C)'),
#    #bargap=0.1,
#    template='seaborn'
#)
#fig2.write_image('Distribución Normal Arpto.png', width=800, height=500, scale=4)
#fig.show()