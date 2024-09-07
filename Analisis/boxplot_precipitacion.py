# -*- coding: utf-8 -*-
"""
Created on Wed July 26 00:35:31 2024

Exploración de datos GCM contra datos ERA5-Land de precipitación en cajas de bloxplot

@author: Arturo A. Granada G.
"""

import xarray as xr
import pandas as PD
import numpy as NP
import plotly.express as PX
import plotly.graph_objects as GO

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

ds1 = xr.open_dataset(r1)
ds2 = xr.open_dataset(r2)
ds3 = xr.open_dataset(r3)
ds4 = xr.open_dataset(r4)

df5 = PD.read_csv(r5, sep=',')
df5['Fecha'] = PD.to_datetime(df5['Fecha'], format='%Y-%m-%d %H:%M:%S')
df5.set_index('Fecha', inplace=True)
df5 = df5.resample('h').sum().reset_index()

df6 = PD.read_csv(r6, sep=',')
df6['Fecha'] = PD.to_datetime(df6['Fecha'], format='%Y-%m-%d %H:%M:%S')
df6.set_index('Fecha', inplace=True)
df6 = df6.resample('ME').sum().reset_index()

df7 = PD.read_csv(r7, sep=',')
df7['Fecha'] = PD.to_datetime(df7['Fecha'], format='%Y-%m-%d %H:%M:%S')
df7.set_index('Fecha', inplace=True)
df7 = df7.resample('ME').sum().reset_index()

df8 = PD.read_csv(r8, sep=',')
df8['Fecha'] = PD.to_datetime(df8['Fecha'], format='%Y-%m-%d %H:%M:%S')
df8.set_index('Fecha', inplace=True)
df8 = df8.resample('ME').sum().reset_index()

df9 = PD.read_csv(r9, sep=',')
df9['Fecha'] = PD.to_datetime(df9['Fecha'], format='%Y-%m-%d %H:%M:%S')
df9.set_index('Fecha', inplace=True)
df9 = df9.resample('ME').sum().reset_index()

df10 = PD.read_csv(r10, sep=',')
df10['Fecha'] = PD.to_datetime(df10['Fecha'], format='%Y-%m-%d %H:%M:%S')
df10.set_index('Fecha', inplace=True)
df10 = df10.resample('ME').sum().reset_index()

df11 = PD.read_csv(r11, sep=',')
df11['Fecha'] = PD.to_datetime(df11['Fecha'], format='%Y-%m-%d %H:%M:%S')
df11.set_index('Fecha', inplace=True)
df11 = df11.resample('ME').sum().reset_index()
#print(df5)
''' Promediamos por mes'''
mes_GCM119 = ds1.resample(time='ME').sum()
mes_GCM126 = ds2.resample(time='ME').sum()
mes_GCM245 = ds3.resample(time='ME').sum()
mes_Era = ds4.resample(time='ME').sum()
#print(mes_Era['time'].head(50))
'''Seleccionamos las variables y periodo de estudio'''
f_i = '2015-01-01 01:30:00'
f_f = '2023-12-31 23:00:00'

p_119 = mes_GCM119['pr'] * 86400
p_126 = mes_GCM126['pr'] * 86400
p_245 = mes_GCM245['pr'] * 86400
p_ERA = mes_Era['precipitation_hourly'] / 0.01
p1_ERA = ds4['precipitation_hourly'] / 0.01

p_119.attrs['units'] = 'mm/day'
p_126.attrs['units'] = 'mm/day'
p_245.attrs['units'] = 'mm/day'
p_ERA.attrs['units'] = 'mm/day'
p1_ERA.attrs['units'] = 'mm/day' 

p_119 = p_119.loc[f_i:f_f]
p_126 = p_126.loc[f_i:f_f]
p_245 = p_245.loc[f_i:f_f]
p_ERA = p_ERA.loc[f_i:f_f]
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

lon_ERA_pacifico = -76.9869 #-76.5647
lat_ERA_pacifico = 3.8480 #3.6451

p_GCM_119 = p_119.sel(lon=lon_GCM, lat=lat_GCM, method='nearest')
p_GCM_126 = p_126.sel(lon=lon_GCM, lat=lat_GCM, method='nearest')
p_GCM_245 = p_245.sel(lon=lon_GCM, lat=lat_GCM, method='nearest')
p_ERA_arpto = p_ERA.sel(longitude=lon_ERA_arpto, latitude=lat_ERA_arpto, method='nearest')
p1_ERA_arpto = p1_ERA.sel(longitude=lon_ERA_arpto, latitude=lat_ERA_arpto, method='nearest')

p_ERA_farallones = p_ERA.sel(longitude=lon_ERA_farallones, latitude=lat_ERA_farallones, method='nearest')
p_ERA_cumbre = p_ERA.sel(longitude=lon_ERA_cumbre, latitude=lat_ERA_cumbre, method='nearest')
p_ERA_diana = p_ERA.sel(longitude=lon_ERA_diana, latitude=lat_ERA_diana, method='nearest')
p_ERA_siloe = p_ERA.sel(longitude=lon_ERA_siloe, latitude=lat_ERA_siloe, method='nearest')
p_ERA_univalle = p_ERA.sel(longitude=lon_ERA_univalle, latitude=lat_ERA_univalle, method='nearest')
p_ERA_pacifico = p_ERA.sel(longitude=lon_ERA_pacifico, latitude=lat_ERA_pacifico, method='nearest')

pre_GCM_119 = p_GCM_119.to_dataframe().reset_index() 
pre_GCM_126 = p_GCM_126.to_dataframe().reset_index()
pre_GCM_245 = p_GCM_245.to_dataframe().reset_index()

pre_Era_arpto = p_ERA_arpto.to_dataframe().reset_index()
pre1_Era_arpto = p1_ERA_arpto.to_dataframe().reset_index()

pre_Era_farallones = p_ERA_farallones.to_dataframe().reset_index()
pre_Era_cumbre = p_ERA_cumbre.to_dataframe().reset_index()
pre_Era_diana = p_ERA_diana.to_dataframe().reset_index()
pre_Era_siloe = p_ERA_siloe.to_dataframe().reset_index()
pre_Era_univalle = p_ERA_univalle.to_dataframe().reset_index() 
pre_Era_pacifico = p_ERA_pacifico.to_dataframe().reset_index()

pre1_Era_arpto.to_csv('Precipitacion ERA Arpto.csv', sep=';')
#df5.to_csv('Precipitacion Obs Arpto.csv', sep=';')
'''Correlación'''
cor_arpto = pre_Era_arpto['precipitation_hourly'].corr(df5['Ptotal'])
print(f'Correlacion Era Arpto: {cor_arpto}')

#pre_GCM_119['time'] = PD.to_datetime(pre_GCM_119['time'], format='%Y-%m-%d %H:%M:%S')
#pre_GCM_126['time'] = PD.to_datetime(pre_GCM_126['time'], format='%Y-%m-%d %H:%M:%S')
#pre_GCM_245['time'] = PD.to_datetime(pre_GCM_245['time'], format='%Y-%m-%d %H:%M:%S')
#pre_GCM_119['mes'] = pre_GCM_119['time'].dt.month
#pre_GCM_126['mes'] = pre_GCM_126['time'].dt.month
#pre_GCM_245['mes'] = pre_GCM_245['time'].dt.month

##print(pre_GCM_245.describe())
##print(pre_Era_pacifico.describe())
##print(df11.describe())

#pre_Era_arpto['mes'] = pre_Era_arpto['time'].dt.month
#pre_Era_farallones['mes'] = pre_Era_farallones['time'].dt.month
#pre_Era_cumbre['mes'] = pre_Era_cumbre['time'].dt.month
#pre_Era_diana['mes'] = pre_Era_diana['time'].dt.month
#pre_Era_siloe['mes'] = pre_Era_siloe['time'].dt.month
#pre_Era_univalle['mes'] = pre_Era_univalle['time'].dt.month
#pre_Era_pacifico['mes'] = pre_Era_pacifico['time'].dt.month

#df5['mes'] = df5['Fecha'].dt.month
#df6['mes'] = df6['Fecha'].dt.month
#df7['mes'] = df7['Fecha'].dt.month
#df8['mes'] = df8['Fecha'].dt.month
#df9['mes'] = df9['Fecha'].dt.month
#df10['mes'] = df10['Fecha'].dt.month
#df11['mes'] = df11['Fecha'].dt.month

'''Salida express'''
#fig = PX.box(pre_GCM_119, x='mes', y='pr',
#             labels={'x': 'Mes', 'pr': 'Precipitación Promedio'},
#             title='Boxplot de Promedios Mensuales de Precipitación')
#fig.show()

'''Salida multiple'''
#fig = GO.Figure()

#fig.add_trace(GO.Box(x=pre_GCM_119['mes'], y=pre_GCM_119['pr'], boxmean=True, name='SSP1-1.9', marker_color='#00CC96'))
#fig.add_trace(GO.Box(x=pre_GCM_126['mes'], y=pre_GCM_126['pr'], boxmean=True, name='SSP1-2.6', marker_color='#636EFA'))
#fig.add_trace(GO.Box(x=pre_GCM_245['mes'], y=pre_GCM_245['pr'], boxmean=True, name='SSP2-4.5', marker_color='#EF553B'))

#fig.add_trace(GO.Box(x=pre_Era_arpto['mes'], y=pre_Era_arpto['precipitation_hourly'], boxmean=True, name='Arpto')) #, marker_color='#636EFA'
#fig.add_trace(GO.Box(x=df5['mes'], y=df5['Ptotal'], boxmean=True, name='Observación', marker_color='#EF553B'))

#fig.add_trace(GO.Box(x=pre_Era_farallones['mes'], y=pre_Era_farallones['precipitation_hourly'], boxmean=True, name='Farallones')) #, marker_color='#636EFA'
#fig.add_trace(GO.Box(x=df6['mes'], y=df6['Ptotal'], boxmean=True, name='Observación', marker_color='#EF553B'))

#fig.add_trace(GO.Box(x=pre_Era_cumbre['mes'], y=pre_Era_cumbre['precipitation_hourly'], boxmean=True, name='La Cumbre')) # , marker_color='#636EFA'
#fig.add_trace(GO.Box(x=df7['mes'], y=df7['Ptotal'], boxmean=True, name='Observación', marker_color='#EF553B'))

#fig.add_trace(GO.Box(x=pre_Era_diana['mes'], y=pre_Era_diana['precipitation_hourly'], boxmean=True, name='La Diana')) #, marker_color='#636EFA'
#fig.add_trace(GO.Box(x=df8['mes'], y=df8['Ptotal'], boxmean=True, name='Observación', marker_color='#EF553B'))

#fig.add_trace(GO.Box(x=pre_Era_siloe['mes'], y=pre_Era_siloe['precipitation_hourly'], boxmean=True, name='Siloe')) #, marker_color='#636EFA'
#fig.add_trace(GO.Box(x=df9['mes'], y=df9['Ptotal'], boxmean=True, name='Observación', marker_color='#EF553B'))

#fig.add_trace(GO.Box(x=pre_Era_univalle['mes'], y=pre_Era_univalle['precipitation_hourly'], boxmean=True, name='Univalle')) #, marker_color='#636EFA'
#fig.add_trace(GO.Box(x=df10['mes'], y=df10['Ptotal'], boxmean=True, name='Observación', marker_color='#EF553B'))

#fig.add_trace(GO.Box(x=pre_Era_pacifico['mes'], y=pre_Era_pacifico['precipitation_hourly'], boxmean=True, name='Unipacífico')) #, marker_color='#636EFA'
#fig.add_trace(GO.Box(x=df11['mes'], y=df11['Ptotal'], boxmean=True, name='Observación', marker_color='#EF553B'))

''' Nombres de los meses '''
#meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

#fig.update_layout(
#    title='Precipitación total por mes, "ERA5-Land"',
#    title_font_size = 22,
#    yaxis_title='Precipitación total (mm/mes)',
#    xaxis_title='Mes',
#    xaxis=dict(
#        tickvals=list(range(1, 13)), # Valores de tick correspondientes a los números de mes
#        ticktext=meses               # Etiquetas de texto correspondientes a los nombres de los meses
#    ),
#    template='seaborn',
#    boxmode='group' # group together boxes of the different traces for each value of x
#)
#fig.write_image('Precipitacion total ERA5-Land.png', width=800, height=500, scale=4)
#fig.show()

'''Diagrama de barras'''
#fig = GO.Figure()
#fig.add_trace(GO.Bar(x=pre_GCM_119['mes'], y=pre_GCM_119['pr'], name='SSP1-1.9', marker_color='#00CC96'))
#fig.add_trace(GO.Bar(x=pre_GCM_126['mes'], y=pre_GCM_126['pr'], name='SSP1-2.6', marker_color='#636EFA'))
#fig.add_trace(GO.Bar(x=pre_GCM_245['mes'], y=pre_GCM_245['pr'], name='SSP2-4.5', marker_color='#EF553B'))
#fig.show()