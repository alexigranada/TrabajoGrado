# -*- coding: utf-8 -*-
"""
Created on Wed July 23 20:43:20 2024

Exploración de distribución de datos GCM contra datos ERA

@author: Arturo A. Granada G.
"""

import pandas as PD
import plotly.express as px

r1 = 'Datos/V_Climaticas_Arpto_Medicion_ERA.csv'

df = PD.read_csv(r1, sep=',')

df['Fecha'] = PD.to_datetime(df['Fecha'], format='%Y-%m-%d %H:%M:%S')
print(df)

fig = px.histogram(df, x='Tmedia', marginal='box')
fig.show()