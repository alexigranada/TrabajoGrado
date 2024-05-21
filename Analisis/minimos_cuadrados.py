# -*- coding: utf-8 -*-
"""
Created on Wed Apr  01 12:35:33 2024

Ajuste de mínimos cuadrados, linea de tendencia para las variables.
El coeficiente m es la pendiente de la línea de tendencia, que indica cuánto cambia la temperatura multianual promedio para cada unidad de cambio en la temperatura (dia, semanal, mensual).
El coeficiente b es el término independiente, que indica el valor esperado de la temperatura multianual promedio cuando la temperatura (día, semanal, mensual) es cero.
@author: Arturo A. Granada G.
"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go

#t_d = [30.4,31,30.2,26.6,28.8,30,28.6,30.4,30.4,29.4,28.4,30.6,30.2,31.4,31,30.4,30,30.6,31.2,31,31.6,31.2,32,26.8,29.6,31.6,30.4,31.2,30,29.4,27.2,31.2,31,30,31,30.4,30.2,31.2,31,31,30,30.4,31.4,27.8,29,32.4,32.4,31.6,29.2,31,30.8,29.2,30,30.8,28.4,31.2,31.2,26.4,29.6,31.6,29.8,27.6,31.8,30,28,31.4,29.8,30.2,30.4,30.6,31.6,29.2,30.2,31.8,31,27,28,30,29.8,30.4,30.4,29.6,30,27.6,25.6,32.4,31.4,30.2,30.4,26.8,31.2,28,31,29.8,31.4,31.2,31.6,28.8,31.4,31.4,32,29.4,30.8,29.2,30.6,25.6,28.4,29,33.4,30.6,31.8,31,31,31.2,31,31.8,32,32.6,31.2,32.2,29.8,30.2,30.8,31.2,29.8,29.4,30.6,31.2,32,29.4,32.2,28,27.8,29.4,29.2,31.4,30.8,30.8,28,31,27.8,31,29.2,31,31,30.8,28.8,30.4,31.8,31.4,26.6,26.2,27.6,31,31.2,26.4,31.8,31.2,31,30.6,31,31.6,30.6,30.4,28.2,29,27.2,29,30.6,30.6,31.2,31,31,29.8,32.2,32,30,30.8,29.8,30,31,30.2,30.2,30.8,31.6,32.2,29.6,29.8,28.4,31.4,31.4,30.2,30.8,30.6,30.2,31.8,31.6,31.6,30.6,31.4,31,29.2,31.2,29.2,31.4,29.8,29.8,27.4,29.6,27.2,30.4,30.2,29.6,28.4,30.8,31.8,30.6,29,29.2,29,28.4,31.2,30.8,31,30,30.4,29.8,28.8,29.6,31.2,30.2,31.2,30.4,29.2,30.6,29.2,29.4,30.2,30.2,28.6,30.4,30.4,32,28.6,29.6,29.4,31.6,30.4,31.6,30,31.4,31.6,28.6,29.4,29.4,28.6,29,29.6,31.4,31.4,28.2,30.8,26.4,30.2,29.8,27,30,30,29.2,27.2,30,30.8,30.4,31,30,30.6,31,26.8,31.6,27.6,32,30,27.6,27.2,30.6,31.2,30.4,29.4,29.2,28.4,28.8,30.4,27,30.4,29.2,31,28.8,29,29.8,27.8,28.2,29.6,28.8,27.2,30.6,30.6,24.6,28.8,29.2,26.6,31,28.4,30.2,27.2,29.4,30.6,25.4,27,31,30.2,26.8,29.4,30.2,27.6,32,31.8,27.8,29.8,30.2,31.4,29.6,31,29.4,30,28.2,29.8,29.6,26.2,30.8,27.4,29.6,28,26.6,30,30.6,27.2,29.4]
#t_ma = [30.36,29.83,30.275,30.095,29.94,30.32,30.775,30.418,30.815,30.461,29.988,30.377,30.114,30.421,30.574,30.527,30.257,30.657,30.344,30.972,30.72,30.6,30.33,30.32,30.5,30.54,30.52,30.15,30.07,30.9,30.52,30.49,30.4,30.44,30.7,31.04,30.26,30.54,30.6,30.875,30.644,30.766,30.663,31.103,31.1,30.826,31.146,30.441,31.031,30.757,30.856,30.922,30.604,30.75,30.671,30.69615385,30.9,30.97083333,31.06818182,30.61538462,30.92692308,30.86,30.82307692,30.98076923,30.7,31.04166667,30.37777778,30.63214286,31.248,30.88461538,31.01538462,31.068,30.29583333,30.91666667,30.66551724,30.752,31.24615385,30.93043478,31.11481481,30.84615385,31.032,30.85217391,30.70769231,30.58846154,30.82,30.88846154,31.236,31.13043478,30.9962963,31.144,31.08571429,30.968,31.15384615,30.98846154,30.7625,30.95555556,30.76538462,30.65217391,31.18076923,30.82857143,30.776,30.88571429,31.1962963,30.76923077,31.53703704,30.43571429,30.45,31.1875,31.06923077,30.74,30.89230769,31.3,30.86896552,31.04583333,31.29230769,31.17777778,31.084,31.73913043,30.89259259,31.32857143,31.16333333,30.83793103,31.24,31.06923077,31.24814815,30.71923077,30.59230769,30.74074074,30.61,30.90769231,30.77857143,31.08666667,30.9962963,31.0137931,30.80714286,30.61724138,30.608,30.56071429,30.51785714,30.60357143,30.70689655,30.74137931,31.09655172,30.98518519,30.8875,30.49655172,30.72413793,30.78148148,31.07241379,30.38,30.54642857,30.45666667,30.47777778,30.77407407,30.46071429,30.38928571,30.28214286,30.55,30.69230769,30.528,30.46923077,30.86428571,30.7,30.25555556,30.37692308,30.916,30.592,30.73571429,31.12857143,30.39230769,30.51071429,30.39583333,30.09655172,30.43333333,30.36071429,30.23846154,30.66296296,30.25357143,30.66428571,30.37777778,30.48076923,30.52962963,30.72962963,30.23103448,30.30740741,30.59230769,30.45714286,30.26296296,30.54642857,30.74074074,30.5,29.86923077,30.67857143,30.64444444,30.79642857,30.24814815,30.40384615,30.92592593,30.36206897,30.47857143,30.65172414,30.64230769,30.71851852,30.672,30.616,30.13103448,30.39259259,30.332,29.64814815,30.728,30.38846154,30.08518519,30.27777778,30.11428571,30.55384615,30.96538462,30.79615385,30.584,30.63928571,30.72592593,30.512,30.77777778,30.71071429,30.57142857,30.32692308,30.74814815,30.47142857,30.38928571,30.17037037,30.36296296,30.59230769,30.45,30.35357143,30.59285714,30.55384615,30.18518519,30.66923077,30.43928571,30.148,30.24642857,29.94482759,30.08461538,30.412,30.29655172,30.21785714,30.10689655,30.27586207,30.24827586,30.2962963,29.68571429,30.46296296,30.2962963,30.53214286,29.86666667,30.42962963,29.80689655,30.64074074,30.41785714,30.09166667,29.88148148,30.22962963,30.28571429,29.79285714,30.15357143,30.39285714,30.06296296,30.4,30.31851852,30.07142857,29.85357143,30.25,30.06428571,30.15925926,29.24074074,30.55925926,30.04444444,29.65862069,29.86206897,30.22142857,30.27777778,30.36666667,29.75,29.55862069,30.08076923,30.12222222,29.98461538,29.67407407,29.82857143,30.11481481,29.75555556,30.164,29.80769231,29.56666667,29.70740741,29.91851852,30.01034483,29.96666667,29.78888889,29.65555556,29.53076923,29.35172414,29.82222222,29.40714286,29.68461538,29.81034483,29.92413793,29.58965517,29.68928571,29.97241379,29.75714286,29.75,29.76538462,30.12692308,30.14074074,29.81851852,30.30769231,29.50333333,29.35517241,29.95862069,29.86666667,29.96206897,30.33214286,29.76296296,29.9,29.92666667,29.54,29.44444444,29.91333333,29.68518519,29.85,29.3,30.00344828,30.02307692,30.21851852,29.85,30.29310345,29.86206897,29.976,30.236,29.98148148,29.95185185,30.26296296,30.55925926,30.15,30.39285714,30.08666667,30.21923077]


''' Convertimos lista a Arrays numpy '''
#t_d = np.array(t_d)
#t_ma = np.array(t_ma)

''' Importamos Datos'''
#ruta_e5 = 'Datos/ERA5/LaCumbre/ERA5_LaCumbre_Hora.csv' #Ruta del archivo ERA5
#ruta_estacion = 'Datos/Hora/V_Climaticas_LaCumbre_RL_Hora.csv' #Ruta del archivo Estatción
#ruta = 'Datos/Cumbre_12_Hora.csv'
ruta = 'Datos/Ajuste_5h_Era5_MC.csv'
#era5 = pd.read_csv(ruta_e5, delimiter=';') #Cargamos archivo
#ruta = 'Datos/ERA5/UPacifico/UP.csv'
#estacion = pd.read_csv(ruta_estacion, delimiter=';')

df = pd.read_csv(ruta, delimiter=';')
print(df)
df['Fecha (UTC-05:00)'] = pd.to_datetime(df['Fecha (UTC-05:00)'], format='%d/%m/%Y %H:%M')
##t_d = df['Temp Media']#[:2000]
##t_ma = df['ERA5']#[:2000]

'''Promediamos o sumamos por hora'''
#df.set_index('Fecha (UTC-05:00)', inplace=True)
#df12 = df.resample('12h').mean()
#df12.reset_index(inplace=True)

''' Paso No 2'''
t_d =  df['Temp Media']
t_ma =  df['temperature_2m']

##t_d = np.array(t)
##t_ma = np.array(ta)

#print(t_d)

''' Exportar el DataFrame a un archivo CSV '''
#title = f'UP_12_Hora.csv'
#df12.to_csv(title, sep=';', index=False)

''' Creamos matrix A de diseño con con temperatura diaria y termino independiente'''
A = np.vstack([t_d, np.ones(len(t_d))]).T
##Y = t_ma.reshape(-1, 1)

''' Calcular el ajuste de minimos cuadrados'''
m, b = np.linalg.lstsq(A, t_ma, rcond=None)[0]
##coeficientes = np.linalg.inv(A.T @ A) @ A.T @ Y
##m, b = coeficientes.flatten()
''' Imprimimos los coeficientes de la linea de tendencia'''
print(f'Coeficiente (m): {m}')
print(f'Término independiente (b): {b}')

'''Ploteamos la gráfica'''
fig = go.Figure()
fig.add_trace(go.Scatter(x=t_d, y=t_ma, mode='markers', name='Valores reales - Valores ERA5', marker=dict(size=4)))
fig.add_trace(go.Scatter(x=t_d, y=m*t_d+b, mode='lines', name='Línea de tendencia ajustada'))
fig.update_layout(title ='Correlación de Temperatura entre estación U. Pacífico y ERA5-Land, ',
                  xaxis = dict(title='Temperatura estación U. Pacífico (Hora)'),
                  yaxis = dict(title='Temperatura hora ERA5-Land (Hora)'),
                  title_x = 0.5,
                  title_font_size=22,
                  template = 'seaborn')
#fig.show()
fig.write_image("MC_temperatura_era5_UP.png", width=800, height=500, scale=4)
''' Calcular predicciones '''
prediccion = m * t_d + b

''' Calculamos error cuadratico para cada valor'''
error2 = (t_ma - prediccion) ** 2
ecm = np.mean(error2) #Calculamos la media de esos errores 'ECM'

''' Calculamos el error absoluto'''
error_abs = np.abs(t_ma - prediccion)
eam = np.mean(error_abs)

''' Calculamos el coeficiente de correlación'''
c_c = np.corrcoef(t_ma, prediccion)[0,1]

print(f'Error Cuadrático Medio EMC: {ecm}')
print(f'Error Absoluto Medio: {eam}')
print(f'Coeficiente de correlación: {c_c}')

#correlacion = t_d.corr(t_ma)
#print('Correlacion Person Estacion La Cumbre vs ERA5 (Temperatura)', correlacion)
#print('Finalizado con exito.')