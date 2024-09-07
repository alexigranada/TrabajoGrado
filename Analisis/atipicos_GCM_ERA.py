# -*- coding: utf-8 -*-
"""
Created on Wed July 23 20:43:20 2024

Exploración de distribución de datos GCM contra datos ERA

@author: Arturo A. Granada G.
"""

import xarray as xr
import pandas as PD
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots

r1 = 'Datos/GCM/tas_3hr_GFDL-ESM4_ssp245_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'
r2 = 'Datos/ERA5_Land_T_P/ERA5-Land_2015_2023_ValleDelCauca_3H.nc'
r3 = 'Datos/UV_5.csv'
#V_Climaticas_Arpto_Medicion_ERA
#Farallones_5
#Cumbre_5
#Diana_5
#Siloe_5
#UP_5
#UV_5

ds1 = xr.open_dataset(r1)
ds2 = xr.open_dataset(r2)
df = PD.read_csv(r3, sep=';')
df['Fecha'] = PD.to_datetime(df['Fecha'], format='%Y-%m-%d %H:%M:%S')
df.set_index('Fecha', inplace=True)
df = df.resample('3h').mean().reset_index()
df_estacion = df.dropna(subset=['Tmedia'])

'''Seleccionamos las variables y periodo de estudio'''
f_i = '2015-01-01 03:00'
f_f = '2023-12-31 21:00'

temp_GCM = ds1['tas'].loc[f_i:f_f]
temp_ERA = ds2['t2m'].loc[f_i:f_f]
temp_ERA = temp_ERA.loc[~((temp_ERA['time'].dt.month==2) & (temp_ERA['time'].dt.day == 29))]

''' Seleccionamos pixel de interes en el GCM '''
lon_GCM = 283.1
lat_GCM = 3.5
t_GCM = temp_GCM.sel(lon=lon_GCM, lat=lat_GCM, method='nearest')
#print(temp_GCM)

'''Seleccionamos el pixel de interes en ERA5'''
lon_ERA = -76.5338
lat_ERA = 3.3777
t_ERA = temp_ERA.sel(longitude=lon_ERA, latitude=lat_ERA, method='nearest')

'''Función K a C'''

def k_c (k):
    c = k - 273.15
    return c

df_GCM = t_GCM.to_dataframe().reset_index()
df_ERA = t_ERA.to_dataframe().reset_index()

df_GCM['tas'] = df_GCM['tas'].apply(k_c)
df_ERA['t2m'] = df_ERA['t2m'].apply(k_c)

print(df_GCM.describe())
print(df_ERA.describe())
print(df_estacion.describe())

df_GCM = df_GCM.rename(columns={'tas': 'Temperatura'})
df_ERA = df_ERA.rename(columns={'t2m': 'Temperatura'})
df_estacion = df_estacion.rename(columns={'Tmedia': 'Temperatura'})
#print(df_GCM)
#print(df_ERA)

#df_GCM.to_csv('GCM.csv', sep=';')
#df_ERA.to_csv('ERA.csv', sep=';')

'''Creamos una etiqueta para cada temperatura'''
df_GCM['Fuente'] = 'GFDL-ESM4'
df_ERA['Fuente'] = 'ERA5-Land'
df_estacion['Fuente'] = 'Observación'

'''Combinamos los DF'''
df_union = PD.concat([df_estacion, df_GCM, df_ERA], ignore_index=True)
##df_final = df_union[]
#print(df_union)

''' Crear una figura de subtramas con Plotly'''
#fig = px.histogram(df_union, 
#                   x='Temperatura', 
#                   marginal='box', 
#                   color='Fuente', 
#                   opacity=0.75,
#                   color_discrete_sequence=['#00CC96', '#EF553B', '#636EFA'])# '#2BCDC1', '#835AF1', '#7FA6EE' opacity=0.75
#fig.update_layout(
#    title='Distribución temperatura Estación "Arpto"',
#    title_font_size = 22,
#    yaxis = dict(title='Número de Datos'),
#    xaxis = dict(title='Temperatura (°C)'),
#    bargap=0.1,
#    template='seaborn'
#)
#fig.write_image('Distribución Box Arpto.png', width=800, height=500, scale=4)
#fig.show()

'''Distribución normal con curva'''
#x1 = df_GCM['tas']
#x2 = df_ERA['t2m']
hist_data = [df_ERA['Temperatura'], df_GCM['Temperatura'], df_estacion['Temperatura']]
group_labels = ['ERA5-Land', 'GFDL-ESM4', 'Observación']
colors = ['#636EFA', '#EF553B', '#00CC96', '#7FA6EE', '#B8F7D4']
#colors = ['#7FA6EE', '#835AF1', '#2BCDC1']
#fig2 = ff.create_distplot(hist_data, group_labels, bin_size=0, colors=colors, curve_type='normal')
#fig2.update_layout(
#    title='Distribución temperatura Estación "Arpto"',
#    title_font_size = 22,
#    yaxis = dict(title='Frecuencia'),
#    xaxis = dict(title='Temperatura (°C)'),
#    #bargap=0.1,
#    template='seaborn'
#)
#fig2.write_image('Distribución Normal Arpto.png', width=800, height=500, scale=4)
#fig2.show()

#fig3 = go.Figure()
#fig2.add_trace(go.Box(x=df_ERA['Temperatura'], name='ERA5-Land', boxmean='sd', marker_color='#636EFA'))
#fig2.show()
#fig2 = px.histogram(df_ERA, x='Temperatura', marginal='box')
#fig2.show()

#fig3 = px.histogram(df_GCM, x='Temperatura', marginal='box')
#fig3.show()

#fig = go.Figure(data=[go.Histogram(
#    x=df_GCM['tas'],
#    xbins=dict(
#        start=0,  # Inicio de los bins
#        end=35,   # Fin de los bins
#        size=1    # Tamaño de cada bin
#    ),
#    marker=dict(color='blue'),  # Color de las barras
#    opacity=0.75  # Opacidad de las barras
#)])

# Añadir título y etiquetas de ejes
#fig.update_layout(
#    title='Histograma de Ejemplo',
#    xaxis_title='Valores',
#    yaxis_title='Frecuencia',
#    bargap=0.1  # Espacio entre las barras
#)

# Mostrar el histograma
#fig.show()

# Crear la figura con subgráficas
fig = make_subplots(rows=2, cols=1, 
                    #   subplot_titles=("Distribución normal de Temperaturas", "Boxplot de Temperaturas"),
                    vertical_spacing=0.15)

# Añadir la gráfica de distribución
dist_fig = ff.create_distplot(hist_data, group_labels, bin_size=0, colors=colors, curve_type='normal')
# Ajustar el ancho y la separación de las barras
for trace in dist_fig.data:
    fig.add_trace(trace, row=1, col=1)

# Añadir la gráfica de caja
fig.add_trace(go.Box(x=df_estacion['Temperatura'], name='Observación', boxmean=True, marker_color='#00CC96'), row=2, col=1)
fig.add_trace(go.Box(x=df_GCM['Temperatura'], name='GDFL-ESM4', boxmean=True, marker_color='#EF553B'), row=2, col=1)
fig.add_trace(go.Box(x=df_ERA['Temperatura'], name='ERA5-Land', boxmean=True, marker_color='#636EFA'), row=2, col=1)
# Actualizar el diseño de la figura
fig.update_layout(
    #title_text="Análisis de Temperatura, estación 'Arpto'",
    title='Distribución de la temperatura, estación "Univalle"',
    title_font_size = 22,
    yaxis = dict(title='Frecuencia'),
    xaxis = dict(title='Temperatura (°C)'),
    bargap=0.1,
    #bargap=0.1,
    template='seaborn'
    )
fig.write_image('Distribución Univalle.png', width=800, height=500, scale=4)
#fig.show()