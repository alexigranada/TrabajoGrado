# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:33:48 2024
Exploración de variables ambientales de las estaciones del IDEAM
1. Unir tablas (con el mismo regustro por columnas)
2. Eliminar columnas innecesarias
3. Separar por categoria (NombreEstación)
4. Exportar en archivo CSV
@author: Arturo A. Granada g.
"""

'''Importamos librerias'''
import pandas as pd #Leer datos

ruta1 = 'C:/Datos/Estaciones/Día pluviométrico 2000-2023.csv' #Ruta del archivo
#ruta2 = 'C:/Datos/Estaciones/Temp_min_diaria/2.csv' #Ruta del archivo
#ruta3 = 'C:/Datos/Estaciones/Temp_min_diaria/3.csv' #Ruta del archivo
#ruta4 = 'C:/Datos/Estaciones/Temp_min_diaria/4.csv' #Ruta del archivo
#ruta5 = 'C:/Datos/Estaciones/Temp_min_diaria/5.csv' #Ruta del archivo
#ruta2 = 'C:/Datos/Estaciones/Temperatura mín diaria.csv' #Ruta del archivo
data1 = pd.read_csv(ruta1, delimiter=',') #Cargamos archivo
#data2 = pd.read_csv(ruta2, delimiter=',') #Cargamos archivo
#data3 = pd.read_csv(ruta3, delimiter=',') #Cargamos archivo
#data4 = pd.read_csv(ruta4, delimiter=',') #Cargamos archivo
#data5 = pd.read_csv(ruta5, delimiter=',') #Cargamos archivo
#data2 = pd.read_csv(ruta2, delimiter=',') #Cargamos archivo
#print('Registros, columnas:')
#print(data1.shape)
data1.info()
print('Tabulación de los datos:')
print(data1.head()) 
#print(data2.head()) 
#print(data3.head()) 
#print(data4.head()) 
#print(data5.head()) 
'''Pandas busca las variables numericas y nos mostrará información estadistica'''
#print(data.describe())

''' Unimos los df si tienes las mimas columnas'''
#data = pd.concat([data1, data2, data3, data4, data5], axis=0)#
#print(data)

'''Eliminamos información irrelevante de los datos'''
#data1.drop(columns=['Categoria', 'Entidad', 'AreaOperativa', 'Departamento', 'Municipio', 'FechaInstalacion', 'FechaSuspension', 'IdParametro', 'Etiqueta', 'DescripcionSerie', 'Frecuencia', 'Grado', 'Calificador', 'NivelAprobacion'], inplace=True)

''' Agrupar por la columna 'NombreEstación' '''
agrupar_estacion = data1.groupby('NombreEstacion')

''' Convertimos en DataFrame'''
nombre_estacion = pd.DataFrame(agrupar_estacion)
print(nombre_estacion)

## Farallones(4), Juanchaco(5), Siloe(9), UPacifico(), LaCumbre()
## (3)(6)(19)(46)(47)(51)(65)(80)(83)(84)(98)(103)(108)(126)(127)(131)(132)(133)
''' Agrupamos por categoria'''
estacion_x = agrupar_estacion.get_group(str(nombre_estacion[0][133]))# Cambiamos por cada estación
name = str(nombre_estacion[0][133])# Cambiamos por cada estación

''' Exportar el DataFrame por estaciones a un archivo CSV '''
title_file = f'Pluviometrico_dia_{name}.csv'
estacion_x.to_csv(title_file, sep=';', index=False)
print('Archivo Exportado. Fin parte No 1')