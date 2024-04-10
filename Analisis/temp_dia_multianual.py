# -*- coding: utf-8 -*-
"""
Created on Wed Apr  01 12:35:33 2024
Gradiente termico vertical: relación del cambio de temperatura en función de la altura
@author: Arturo A. Granada G.
"""

import pandas as pd
import numpy as np
import math
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

''' Selecionamos los días de cada año (Día Multianual)'''
#print('Aeropuerto Btra')
#year_1 = dato1[dato1['Fecha'].dt.year == 2014]
#mes_1 = year_1[year_1['Fecha'].dt.month == 8]
#dia_1 = mes_1[mes_1['Fecha'].dt.day == 27]
#print(mes_1)
#max_mean_1 = dia_1['ValorMax'].mean()
#print(max_mean_1)

''' Imprimimos el día multianual por mes'''
#year_2 = dato2[dato2['Fecha'].dt.year == 2014]
d_ma_bcalima = [] #Creamos un array para almacenar el calculo díario multianual

for m in range(1,13):
    mes_2 = dato2[dato2['Fecha'].dt.month == m]#Iteramos por mes
    #print(f'mes: {m}')
    for d in range(1,32):    
        dia_2 = mes_2[mes_2['Fecha'].dt.day == d]
        max_mean_2 = dia_2['ValorMax'].mean()
        min_mean_2 = dia_2['ValorMin'].mean()
        d_ma_bcalima.append({'Mes': m, 'Día': d, 'ValorMax': max_mean_2, 'ValorMin': min_mean_2}) #Almacenamos la variable como un diccionario
        #print(max_mean_2)

#year_3 = dato3[dato3['Fecha'].dt.year == 2014]

d_ma_colpuer = []
for m in range(1,13):
    mes_3 = dato3[dato3['Fecha'].dt.month == m]#Iteramos por mes
    #print(f'Mes: {m}')
    for d in range(1,32):    
        dia_3 = mes_3[mes_3['Fecha'].dt.day == d]
        max_mean_3 = dia_3['ValorMax'].mean()
        min_mean_3 = dia_3['ValorMin'].mean()
        d_ma_colpuer.append({'Mes': m, 'Día': d, 'ValorMax': max_mean_3, 'ValorMin': min_mean_3})
        #print(f'Día{d}: {max_mean_3}')

''' Convertimos arreglo en DataFrame'''
df_bc = pd.DataFrame(d_ma_bcalima)
df_cp = pd.DataFrame(d_ma_colpuer)

''' Eliminamos días no validos'''
df_bc = df_bc.dropna().reset_index(drop=True, inplace=False)
df_cp = df_cp.dropna().reset_index(drop=True, inplace=False)# Crea un nuevo indice, pero no lo agrega como columna
#print('B. Calima')
#print(df_bc)
#print('Colpuertos')
#print(df_cp)





















''' Probamos con una regresión lineal multiple'''
#x = mes_1[['ValorMax']]#[:26:]
#y = mes_2['ValorMax']#[:26:]

#print(x)
#print(y)
''' Dividir el conjunto de datos en conjuntos de entrenamiento y prueba '''
#x_train = x[:26:] 
#x_test = x[27::] 
#y_train = y[:26:] 
#y_test = y[27::]

#print(x_test)
#print(x_train)
#print(y_test)
#print(y_train)

''' Iniciamos el modelo de Regresion Lineal'''
#modelo = LinearRegression()

''' Entrenamos el modelo '''
#modelo.fit(x_train, y_train)

''' Realizamos predicciones '''
#y_pred = modelo.predict(x_test)

''' Evaluamos el podelo'''
#print(f'Mean Absolute Error: {metrics.mean_absolute_error(y_test, y_pred)}')
#print(f'Mean Squared Error: {metrics.mean_squared_error(y_test, y_pred)}')
#print(f'Root Mean Squared Error: {np.sqrt(metrics.mean_squared_error(y_test, y_pred))}')
#print(f'Coeficiente de determinación R2: {metrics.r2_score(y_test, y_pred)}')

'''Mostramos los coeficientes de la ecuación'''
#print('Coeficientes del Modelo')
#print(f'Intercepto: {modelo.intercept_}')
#print(f'coeficientes: {modelo.coef_}')

#nuevos_valores = pd.DataFrame({'ValorMax': [32, 32.4, 32.6]})

#predicion = modelo.predict(nuevos_valores)

#print(f'El valor de las nuevas predicciones es: {predicion}')