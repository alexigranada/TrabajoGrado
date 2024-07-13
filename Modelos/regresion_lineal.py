# -*- coding: utf-8 -*-
"""
Created on Wed Jun  24 10:22:44 2024
Creación del modelo de regresión sin el uso de alguna libreria de IA
@author: Arturo A. Granada G.
"""
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

'''Creamos funciones para el calculo del gradiente descendiente'''
def crear_modelo (a,b,x):
    return a*x + b

def ecm (y, Y):
    N = y.shape[0]
    error = np.sum((y - Y) ** 2) / N
    return error

def gradiente_descendente (a_, b_, alpha, x, y):
    N = x.shape[0] #Calculamos la cantidad de datos

    ''' Gradiente: derivada de la función del error conrespecto a los parametros "a" y "b" '''
    da = -(2/N) * np.sum(x * (y - (a_ * x + b_)))
    db = -(2/N) * np.sum(y - (a_ * x + b_))

    ''' Actualizamos los pesos utilizando la formula del gradiente descendiente'''
    a = a_ - alpha * da
    b = b_ - alpha * db

    return a, b

''' Cargamos los datos'''
data = pd.read_csv('Datos/GFDL_Cumbre.csv', sep=',') #skiprows=32 ,usecols=[1,2]
print(data)

fig = px.scatter(data, x='tas119', y='t2mC')
#fig.show()

x = data['tas119'].values
y = data['t2mP'].values

''' Entrenamos el modelo para aprender los coeficientes "a" y "b" '''
'''
Iniciamos "a" y "b" de manera aleatoría, definimos alpha y el numero de iteraciones
Iniciamos una tasa de aprendizaje pequeña para garanrizar la convergecia del algoritmo
'''
np.random.seed(2) #Para la reproducibilidad del entrenamiento
a = np.random.randn(1)[0]
b = np.random.randn(1)[0]

alpha = 0.0004
nits = 1000000

'''Iniciamos el entrenamiento '''
error = np.zeros((nits, 1))

for i in range(nits):
    '''Actualiza el valor de los pesos utilizando el gradiente descendiente'''
    [a, b] = gradiente_descendente(a, b, alpha, x, y)

    '''Calculamos el valor de la predicción'''
    Y = crear_modelo(a, b, x)

    '''Actualiza el valor del error'''
    error[i] = ecm(y, Y)   

    '''Imprimir resultados de cada 100 epocas'''
    if (i + 1) % 10000 == 0:
        print(f'Epoca: {i+1}')
        print(f'        a: {a:.3f}, b: {b:.3f}')
        print(f'    error: {error[i]}')
        print('======================================')

print('Proceso finalizado')
