# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:33:48 2024
Exploración de las estaciones del IDEAM y estimaciones ERA5-Land
@author: Arturo A. Granada g.
"""

import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import plotly.graph_objects as go
import plotly.express as px

#r1 = 'Datos/V_Climaticas_Arpto_Medicion_ERA.csv'
#r1 = 'Datos/V_Climaticas_UPacifico_Medicion_ERA.csv'
#r1 = 'Datos/V_Climaticas_LaCumbre_Medicion_ERA.csv'
r1 = 'Datos/V_Climaticas_Farallones_Medicion_ERA.csv'
#r1 = "Datos/V_Climaticas_Diana_Medicion_ERA.csv"
#r1 = "Datos/V_Climaticas_Siloe_Medicion_ERA.csv"
#r1 = "Datos/V_Climaticas_Univalle_Medicion_ERA.csv"
df = pd.read_csv(r1, delimiter=';', index_col='Fecha' ,  parse_dates=['Fecha'], dayfirst=True)

#estacion = df['Tmedia'].dropna()
#era = df['t2mERA'].dropna()

cor_sperman = df['Tmedia'].corr(df['t2m'], method='spearman') 
cor_person = df['Tmedia'].corr(df['t2m'])
r2 = cor_person ** 2

media_obs = df['Tmedia'].mean()
media_era = df['t2m'].mean()

min_obs = df['Tmedia'].min()
min_era = df['t2m'].min()

max_obs = df['Tmedia'].max()
max_era = df['t2m'].max()

print(f'Coeficiente R2: {r2:.3f}')
print(f'Correlación Pearson: {cor_person:.3f}')
print(f'Correlación Spearman: {cor_sperman:.3f}')
print('....::::....')
print(f'Media: {media_obs};{media_era}')
print(f'Mínima: {min_obs};{min_era}')
print(f'Máxaxima: {max_obs}, {max_era}')

#print(df)
#fig = go.Figure()
#fig.add_trace(go.Scatter(x=df['Tmedia'], y=df['t2m'], mode='markers', marker_color='#990099', opacity=0.85))
#fig.update_layout(title = "Correlación de temperatura estación 'Siloe'",
#                  xaxis = dict(title= dict(text='Observaciones Estación (°C)', font=dict(size=22))),
#                  yaxis = dict(title= dict(text='Estimaciones ERA5-Land (°C)', font=dict(size=22))),
#                  template='seaborn',
#                  title_font_size=26,
#                  title_x = 0.5)
##fig.show()
#fig.write_image("Correlación_Siloe_Era_Obs.png", width=800, height=500, scale=4)

#fig2 = go.Figure()
#fig2.add_trace(go.Scatter(x=df.index, y=df['Tmedia'][2432:2605:], mode='lines', name='Observacion estación', line=dict(color='#E45756')))
#fig2.add_trace(go.Scatter(x=df.index, y=df['t2m'][2432:2605:], mode='lines', name='Estimación ERA5-Land', line=dict(color='#3366CC')))
#fig2.update_layout(title = f"Patron de la temperatura estación 'Siloe'",
#                  xaxis = dict(title= dict(text='Tiempo (h)', font=dict(size=22))),
#                  yaxis = dict(title= dict(text='Temperatura (°C)', font=dict(size=22))),
#                  title_font_size=26,
#                  title_x = 0.5,
#                  template='seaborn') #'plotly_white' - 'plotly_dark' - 'ggplot2' - 'seaborn - 'simple_white'
#fig2.show()

#fig2.write_image("Patron_Siloe_Era_Obs.png", width=800, height=500, scale=4)
print('Finalizado sin errores')