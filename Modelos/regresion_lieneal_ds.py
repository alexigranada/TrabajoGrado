# -*- coding: utf-8 -*-
"""
Created on Wed Jun  26 14:53:55 2024
Creación del modelo de regresión sin el uso de alguna libreria de IA
@author: Arturo A. Granada G.
"""

import xarray as xr
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

r1 = 'Datos/tas_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca_11Km_Mask.nc'
r2 = 'Datos/ERA5-Land_2015_2023_ValleDelCauca_3H_Mask.nc'

ds1 = xr.open_dataset(r1)
ds2 = xr.open_dataset(r2)

'''Crear rango de fecha omitiendo los días bisiestos'''
f1 = '2015-01-01 03:00:00'
f2 = '2035-01-01 00:00:00'
fnormal = pd.date_range(f1, f2, freq='3h')
fecha = fnormal[~((fnormal.month == 2) & (fnormal.day == 29))]
#print(fecha)

'''Adignamos el rango de fecha a los GCM'''
tas = ds1['tas']
tas['time'] = fecha
t2m = ds2['t2m']

temperatura_gcm = tas.sel(time=slice('2015-01-01', '2023-12-31'))

t2m = t2m.loc[f1:f2]
temperatura_era = t2m.loc[~((t2m['time'].dt.month == 2) & (t2m['time'].dt.day == 29))]

''' Canvertimos las variables a DataFrame y reseteamos por indice fecha'''
df_tas = temperatura_gcm.to_dataframe(name='GFDL_tas').reset_index()
df_t2m = temperatura_era.to_dataframe(name='ERA_t2m').reset_index()

'''Eliminamos valores nulos'''
df_tas = df_tas.dropna()
df_t2m = df_t2m.dropna()

'''Preparamos los datos de predición y respuesta'''
''' Selecionamos los valores de predictores X (GCM) y respuestas y (ERA5)'''
X = df_tas['GFDL_tas'].values.flatten()[:, np.newaxis]
y = df_t2m['ERA_t2m'].values.flatten()

''' Creamos la función Modelo '''
model = LinearRegression()

''' Entrenamos modelo '''
model.fit(X, y)

'''Validamos el modelo'''
y_predicion = model.predict(X)

mse = mean_squared_error(y, y_predicion)
r2 = r2_score(y, y_predicion)

print(f'Error cuadrático medio: {mse}')
print(f'Coeficiente R2: {r2}')

'''Imprimimos los'''
