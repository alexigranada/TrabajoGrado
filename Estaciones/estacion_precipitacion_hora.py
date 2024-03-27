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

rutahora = 'D:/Python_TG/Estaciones/Precipitación horaria.csv' #Ruta del archivo
data_hora = pd.read_csv(rutahora, delimiter=';') #Cargamos archivo
print('Registros, Columnas:')
print(data_hora.shape)
print('Tabulación de los datos:')
print(data_hora.head()) 
'''Miramos las variables categoricas y numericas'''
data_hora.info()
'''
object seria una varible de tipo categoria
int64 entero 
float64 real
'''
'''Pandas busca las variables numericas y nos mostrará información estadistica'''
#print(data_hora.describe())

'''Si la desviación estantar (std) es igual a cero, eso quiere decir que los valores numericos no son iguales
Eliminamos información irrelevante de los datos'''
data_hora.drop(columns=['Entidad', 'AreaOperativa', 'Departamento', 'Categoria', 'FechaInstalacion', 'FechaSuspension', 'Frecuencia', 'Grado', 'Calificador', 'NivelAprobacion'], inplace=True)

''' Agrupar por la columna 'NombreEstación' '''
nombre_estacion_hora = data_hora.groupby('NombreEstacion')

'''
for estacion, grupo in estaciones:
    print(f"Grupo para la categoría '{estacion}':")
    print(grupo)
    print("\n")
'''
''' Convertimos en DataFrame'''
grupo_estaciones_hora = pd.DataFrame(nombre_estacion_hora)

''' Agrupamos por categoria'''
estacion_hora = nombre_estacion_hora.get_group(str(grupo_estaciones_hora[0][0]))
#print(estacion_hora['NombreEstacion'])
#print(estacion_hora['Fecha'])

''' Creamos el formato de la fecha'''
fechaformato_hora = "%d/%m/%Y %H:%M"
estacion_hora['Fecha'] = pd.to_datetime(estacion_hora['Fecha'],format=fechaformato_hora)


''' Crear un rango de fechas completo '''
rango_fechas_completo_hora = pd.date_range(start=estacion_hora['Fecha'].min(), end=estacion_hora['Fecha'].max(), freq='H')

#print('Rango Fechas:')
#print(rango_fechas_completo_hora)

''' Crear un DataFrame con las fechas completas '''
df_completo_estacion_hora = pd.DataFrame({'Fecha': rango_fechas_completo_hora})
df_final_estacion_hora = pd.merge(df_completo_estacion_hora, estacion_hora, on='Fecha', how='left')
print('Estación día:')
print(df_final_estacion_hora)

'''' Calculamos los valores nulos'''
valores_nulos_hora = df_final_estacion_hora['Valor'].isnull().sum()
print('Datos faltantes hora: ')
print(valores_nulos_hora)

''' Fusionar los DataFrames en base a la columna 'Fecha'''
#unir_df = pd.merge(df_final_estacion_max, df_final_estacion_min, on='Fecha')
#print('Unión')
#print(unir_df)
''' Sumar las variables correspondientes '''
#unir_df['ValorMedio'] = (unir_df['Valor_x'] + unir_df['Valor_y'])/2
#print(unir_df)

''' Ploteamos las graficas'''

''' Plotly'''
name = str(grupo_estaciones_hora[0][0])
title = f'Patron de la Precipitación estación: {name}'

fig = px.bar(df_final_estacion_hora, x='Fecha', y='Valor', color_discrete_sequence=['darkblue']) #['blue'] - px.colors.qualitative.Dark24

fig.update_layout(title = title,
                  xaxis = dict(title='Hora'),
                  yaxis = dict(title='Precipitación (mm/hora)'),
                  plot_bgcolor='rgba(0,0,0,0)', #Ejes
                  paper_bgcolor='rgba(0,0,0,0)', #Fondo
                  title_x = 0.5)
fig.show()


'''
prec_hora = df_final_estacion_hora['Valor']
time_hora = df_final_estacion_hora['Fecha']
# Crear una figura y ejes
fig, ax = plt.subplots()

# Graficar la precipitación
ax.bar(time_hora, prec_hora, color='blue', alpha=0.7)

# Personalizar el gráfico
ax.set_xlabel('Días')
ax.set_ylabel('Precipitación (mm/dia)')
ax.set_title(title)
plt.show()
#'''