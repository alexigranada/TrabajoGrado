# -*- coding: utf-8 -*-
"""
Created on Wed Apr  01 12:35:33 2024
Calculo de Temperatra Máx y Mín por medio de la temperatura media
@author: Arturo A. Granada G.
"""
import pandas as pd
import plotly.graph_objects as go

r = 'Datos/Estaciones/CVC/Temperatura_Dia_Pacifico-BahiaMalaga[5300000203].csv'
d = pd.read_csv(r, delimiter=';')

print(d.head)

d['Fecha'] = pd.to_datetime(d['Fecha'], format='%d/%m/%Y')

tmax = d['ValorMax']
tmin = d['ValorMin']
tmed = d['ValorMedio']
ttime = d['Fecha']

fig = go.Figure()

fig.add_trace(go.Scatter(x=ttime, y=tmax, mode='lines', name='Temp. Máx', line=dict(color='red')));
fig.add_trace(go.Scatter(x=ttime, y=tmin, mode='lines', name='Temp. Mín', line=dict(color='blue')));
fig.add_trace(go.Scatter(x=ttime, y=tmed, mode='lines', name='Temp. Media', line=dict(color='green')));

fig.show()

