# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:33:48 2024
Exploración de precipitación de las estaciones del IDEAM
@author: Arturo A. Granada G.
"""

'''Importamos librerias'''
import pandas as pd #Leer datos
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt #Graficas y limpiar datos

rutadia = 'C:/Datos/Estaciones/Día pluviométrico 2000-2023.csv' #Ruta del archivo
data_dia = pd.read_csv(rutadia, delimiter=',') #Cargamos archivo
#print('Registros, Columnas:')
#print(data_dia.shape)
#print('Tabulación de los datos:')
#print(data_dia.head()) 
'''Miramos las variables categoricas y numericas'''
#data_dia.info()
'''
object seria una varible de tipo categoria
int64 entero 
float64 real
'''
'''Pandas busca las variables numericas y nos mostrará información estadistica'''
#print(data.describe())

'''Si la desviación estantar (std) es igual a cero, eso quiere decir que los valores numericos no son iguales
Eliminamos información irrelevante de los datos'''
#data_dia.drop(columns=['Entidad', 'AreaOperativa', 'Departamento', 'Categoria', 'FechaInstalacion', 'FechaSuspension', 'Frecuencia', 'Grado', 'Calificador', 'NivelAprobacion'], inplace=True)

''' Agrupar por la columna 'NombreEstación' '''
nombre_estacion_dia = data_dia.groupby('NombreEstacion')

'''
for estacion, grupo in estaciones:
    print(f"Grupo para la categoría '{estacion}':")
    print(grupo)
    print("\n")
'''
''' Convertimos en DataFrame'''
grupo_estaciones_dia = pd.DataFrame(nombre_estacion_dia)

''' Agrupamos por categoria'''
estacion_dia = nombre_estacion_dia.get_group(str(grupo_estaciones_dia[0][137]))
print(estacion_dia)

''' Creamos el formato de la fecha'''
fechaformato_dia = "%m/%d/%Y %H:%M"
estacion_dia['Fecha'] = pd.to_datetime(estacion_dia['Fecha'], format=fechaformato_dia)

''' Crear un rango de fechas completo '''
rango_fechas_completo_dia = pd.date_range(start=estacion_dia['Fecha'].min(), end=estacion_dia['Fecha'].max())
print('Rango Fechas:')
print(rango_fechas_completo_dia)

''' Crear un DataFrame con las fechas completas '''
df_completo_estacion_dia = pd.DataFrame({'Fecha': rango_fechas_completo_dia})
df_final_estacion_dia = pd.merge(df_completo_estacion_dia, estacion_dia, on='Fecha', how='left')
print('Estación día:')
print(df_final_estacion_dia)

'''' Calculamos los valores nulos'''
valores_nulos_dia = df_final_estacion_dia['Valor'].isnull().sum()
print('Datos faltantes día: ')
print(valores_nulos_dia)

''' Ploteamos las graficas'''
prec_dia = df_final_estacion_dia['Valor']
time_dia = df_final_estacion_dia['Fecha']

name = str(grupo_estaciones_dia[0][137])
title = f'Patron día pluviométrico estación: {name}'

''' Crear una figura y ejes '''
fig, ax = plt.subplots()

''' Graficar la precipitación '''
ax.bar(time_dia, prec_dia, color='blue', alpha=0.7)

''' Personalizar el gráfico '''
ax.set_xlabel('Días')
ax.set_ylabel('Precipitación (mm/dia)')
ax.set_title(title)
plt.show()


''' Usando Plotly'''
'''
name = str(grupo_estaciones_dia[0][0])
title = f'Patron de la Precipitación estación: {name}'

fig = px.bar(df_final_estacion_dia, x='Fecha', y='Valor', color_discrete_sequence=px.colors.qualitative.Dark24) #['blue']

fig.update_layout(title = title,
                  xaxis = dict(title='Años'),
                  yaxis = dict(title='Precipitación (mm/día)'),
                  plot_bgcolor='rgba(0,0,0,0)', #Ejes
                  paper_bgcolor='rgba(0,0,0,0)', #Fondo
                  title_x = 0.5)
fig.show()
#'''