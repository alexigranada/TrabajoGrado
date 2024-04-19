# -*- coding: utf-8 -*-
"""
Created on Wed Apr  01 12:35:33 2024
Calculo de Temperatra Máx y Mín por medio de la temperatura media
@author: Arturo A. Granada G.
"""

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

''' Create distplot with custom bin_size'''
#fig = ff.create_distplot(hist_data, group_labels, bin_size=.2)
#fig.show()

fig = ff.create_distplot([df[c] for c in df.columns], df.columns,  marginal="box", bin_size=.25)
fig.show()
print('Finalizado con exito.')


''' Ploteamos la gráfica'''
#fig = go.Figure()

#fig.add_trace(go.Scatter(x=ttime, y=tmax, mode='lines', name='Temp. Máx', line=dict(color='red')));
#fig.add_trace(go.Scatter(x=ttime, y=tmin, mode='lines', name='Temp. Mín', line=dict(color='blue')));
#fig.add_trace(go.Scatter(x=ttime, y=tmed, mode='lines', name='Temp. Media', line=dict(color='green')));

#fig.show()

''' MÉTODO DE DESVIACIÓN ESTANDAR'''

''' Se utiliza cuando los datos tienes una distribuición normal (Forma de campana Gaussiana) 
    Esta distribución se caracteriza por la media y la desviación estandar.
    Rangos:
        1. El 68 % de los datos estan entre media +- DS
        2. el 95 % de los datos estan entre media +- 2DS
        2. el 99.7 % de los datos estan entre media +- 3DS
'''

''' Ploeamos la distribución de los datos '''

