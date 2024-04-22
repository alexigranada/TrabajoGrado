# -*- coding: utf-8 -*-
"""
Created on Wed Apr  01 12:35:33 2024
Calculo de Temperatra Máx y Mín por medio de la temperatura media
@author: Arturo A. Granada G.
"""

''' MÉTODO DE DESVIACIÓN ESTANDAR'''

''' Se utiliza cuando los datos tienes una distribuición normal (Forma de campana Gaussiana) 
    Esta distribución se caracteriza por la media y la desviación estandar.
    Rangos:
        1. El 68 % de los datos estan entre media +- DS
        2. el 95 % de los datos estan entre media +- 2DS
        2. el 99.7 % de los datos estan entre media +- 3DS
'''

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
from plotly.subplots import make_subplots

r = 'Datos/Estaciones/CVC/Temperatura_Dia_Pacifico-BahiaMalaga[5300000203].csv'
d = pd.read_csv(r, delimiter=';')

#print(d.head)

d['Fecha'] = pd.to_datetime(d['Fecha'], format='%d/%m/%Y')

tmax = d['ValorMax']
tmin = d['ValorMin']
tmed = d['ValorMedio']
ttime = d['Fecha']

df = d[['ValorMax','ValorMin', 'ValorMedio']]
df = df.dropna()
#print(df)
#hist_data = [tmax, tmin, tmed]
#group_labels = ['Temp. Máx', 'Temp. Mín', 'Temp. Media']

''' Diagrama de cajas'''

# Crear una figura de subtramas con Plotly
fig = px.histogram(df, x='ValorMin', marginal='box')
fig2 = px.histogram(df, x='ValorMax', marginal='box', color_discrete_sequence = [ '#FF5722' ])
fig3 = px.histogram(df, x='ValorMedio', marginal='box', color_discrete_sequence = [ '#2ECC71' ])
fig.show()
fig2.show()
fig3.show()
print('Finalizado con exito.')






''' Datos con distribución normal '''
#m_min = tmin.mean()
#m_max = tmax.mean()
#m_medio = tmed.mean()

#std_min = tmin.std()
#std_max = tmax.std()
#std_medio = tmed.std()

#lmt_inf_min = m_min - 3*std_min
#lmt_sup_min = m_min + 3*std_min


#fig.add_vline(x=m_min, line_color='black', annotation_text='$\mu$')
#fig.add_vline(x=lmt_inf_min, line_color='red', annotation_text='$\mu-3\sigma$')
#fig.add_vline(x=lmt_sup_min, line_color='red', annotation_text='$\mu+3\sigma$')

''' Create distplot with custom bin_size'''
#fig = ff.create_distplot(hist_data, group_labels, bin_size=.2)
#fig.show()

#fig = ff.create_distplot([df[c] for c in df.columns], df.columns,  marginal="box", bin_size=.25)
#fig.show()

''' Ploteamos la gráfica'''
#fig = go.Figure()

#fig.add_trace(go.Scatter(x=ttime, y=tmax, mode='lines', name='Temp. Máx', line=dict(color='red')));
#fig.add_trace(go.Scatter(x=ttime, y=tmin, mode='lines', name='Temp. Mín', line=dict(color='blue')));
#fig.add_trace(go.Scatter(x=ttime, y=tmed, mode='lines', name='Temp. Media', line=dict(color='green')));

#fig.show()



''' Ploeamos la distribución de los datos '''
#fig = make_subplots(rows=3, cols=1, subplot_titles=('Temperatura Mín.', 'Temperatura Máx.', 'Temperatura Media'))
#fig.add_trace( go.Histogram(x=tmax, y=ttime), row=1, col=1 )#hover_data=df.columns
#fig.add_trace( go.Histogram(x=tmin, y=ttime), row=2, col=1 )#hover_data=df.columns
#fig.add_trace( go.Histogram(x=tmed, y=ttime), row=3, col=1 )#hover_data=df.columns
