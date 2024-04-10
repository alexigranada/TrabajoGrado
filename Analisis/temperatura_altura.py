# -*- coding: utf-8 -*-
"""
Created on Wed Apr  01 12:35:33 2024
Gradiente termico vertical: relación del cambio de temperatura en función de la altura
@author: Arturo A. Granada G.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import plotly.graph_objects as go

''' Carga de datos '''
r1 = 'Datos/Estaciones/IDEAM/Estaciones Dagua/Temperatura dia/Temperatura_dia_AEROPUERTO BUENAVENTUR [53115010].csv'
r2 = 'Datos/Estaciones/IDEAM/Estaciones Dagua/Temperatura dia/Temperatura_dia_BAJO CALIMA [54075020].csv'
r3 = 'Datos/Estaciones/IDEAM/Estaciones Dagua/Temperatura dia/Temperatura_dia_COLPUERTOS [53115020].csv'
r4 = 'Datos/Estaciones/IDEAM/Estaciones Dagua/Temperatura dia/Temperatura_dia_MISION LA [54075040].csv'

dato1 = pd.read_csv(r1, delimiter=';')
dato2 = pd.read_csv(r2, delimiter=';')
dato3 = pd.read_csv(r3, delimiter=';')
dato4 = pd.read_csv(r4, delimiter=';')

''' Ajuste de fecha '''
dato1['Fecha'] = pd.to_datetime(dato1['Fecha'], format='%Y-%m-%d')
dato2['Fecha'] = pd.to_datetime(dato2['Fecha'], format='%Y-%m-%d')
dato3['Fecha'] = pd.to_datetime(dato3['Fecha'], format='%Y-%m-%d')
dato4['Fecha'] = pd.to_datetime(dato4['Fecha'], format='%Y-%m-%d')