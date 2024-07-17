# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:33:48 2024
Exploración de las estaciones del IDEAM y estimaciones ERA5-Land
@author: Arturo A. Granada g.
"""

import pandas as pd
import plotly.graph_objects as go
import plotly.express as ex

r1 = 'Datos/V_Climaticas_UPacifico_Medicion_ERA.csv'
df = pd.read_csv(r1, delimiter=';', index_col='Fecha' ,  parse_dates=['Fecha'], dayfirst=True)

#print(df)

fig = ex.scatter(df, x='Tmedia', y='t2mERA')
fig.update_layout(title = 'Correlación de temperatura Estación Unipacífico',
                  xaxis_title = 'Observaciones Estación (°C)',
                  yaxis_title = 'Estimaciones ERA5-Land (°C)',
                  template='seaborn',
                  title_font_size=22,
                  title_x = 0.5)
#fig.show()
fig.write_image("Correlación_temperatura_Upacifico_Era_Obs.png", width=800, height=500, scale=4)

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=df.index, y=df['Tmedia'][:150:], mode='lines', name='Observacion estación', line=dict(color='#E45756')))
fig2.add_trace(go.Scatter(x=df.index, y=df['t2mERA'][:150:], mode='lines', name='Estimación ERA5-Land', line=dict(color='#3366CC')))
fig2.update_layout(title = f'Patron de la temperatura Unipacífico',
                  xaxis = dict(title='Tiempo (h)'),
                  yaxis = dict(title='Temperatura (°C)'),
                  title_x = 0.5,
                  template='seaborn') #'plotly_white' - 'plotly_dark' - 'ggplot2' - 'seaborn - 'simple_white'
#fig2.show()
#print('Finalizado sin errores')
fig2.write_image("Patron_temperatura_Upacifico_Era_Obs.png", width=800, height=500, scale=4)
