# -*- coding: utf-8 -*-
"""
Created on Wed Apr  01 12:35:33 2024
Calculo de analisis decadal multianual
@author: Arturo A. Granada G.
"""

import pandas as pd
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
#print(dato1)

''' Ajuste de fecha '''
dato1['Fecha'] = pd.to_datetime(dato1['Fecha'], format='%Y-%m-%d')
dato2['Fecha'] = pd.to_datetime(dato2['Fecha'], format='%Y-%m-%d')
dato3['Fecha'] = pd.to_datetime(dato3['Fecha'], format='%Y-%m-%d')
dato4['Fecha'] = pd.to_datetime(dato4['Fecha'], format='%Y-%m-%d')

año = dato2['Fecha'].dt.year.unique()
print(año)

''' Creamos lista para almacenar las decadas por año'''
d_m = []

for a in año:
    ''' Dividir los datos en periodos de 10 días '''
    df_year = dato2[dato2['Fecha'].dt.year == a]# Dividimos los datos por año
    particiones = [grupo for _, grupo in df_year.groupby(pd.Grouper(key='Fecha', freq='10D'))]# Creamos una lista iterable para almacenar cada año en un periodo de 10 días 
    mean = [ i['ValorMedio'].mean() for i in particiones] #Calculo el promedio entre los 10 días
    
    '''Crear diccionario para cada periodo por año'''
    for i, media in enumerate(mean): # El método enumerate recibe los datos como 'clave' : 'valor'
        d_m.append({'Año': a, 'Periodo (10D)': i+1, 'ValorDecadal': media}) # almacenamos cada año como diccionario en el arreglo

'''Convertimos el diccionario en DataFrame'''
df_dm = pd.DataFrame(d_m)
print(df_dm) # [::] para llamar por posición 

''' Calculamos el promedio Decadal Multianual'''
decadal_multianual = df_dm.groupby('Periodo (10D)') # DataFrameGroupBy contiene métodos y atributos que permiten realizar operaciones y cálculos en estos grupos de datos.

mean_d_m = decadal_multianual.mean()
print(mean_d_m)

d_1_m = decadal_multianual.get_group(1)
print(d_1_m)

'''Ploteamos gráficas'''
#v_d = mean_d_m['ValorDecadal']
#serie = mean_d_m['Periodo (10D)'].index

fig = go.Figure()

fig.add_trace(go.Scatter(x=mean_d_m.index, y=mean_d_m['ValorDecadal'], mode='lines', name='Se', line=dict(color='#EF553B')))

fig.update_layout(title = 'Decadal (10 días) Multianual (1990 - 2000)',
                  xaxis = dict(title='Periodo'),
                  yaxis = dict(title='Temperatura promedio (°C)'),
                  title_x = 0.5,
                  template='plotly_white') #'plotly_white' - 'plotly_dark' - 'ggplot2' - 'seaborn - 'simple_white'
fig.show()

print('Finalizado...')
'''Ploteamos gráficas'''
'''
aer_bv = df1['ValorMedio']
b_c = df2['ValorMedio']
col_pto = df3['ValorMedio']
la_mis = df4['ValorMedio']
time = df2['Fecha']

fig = go.Figure()

fig.add_trace(go.Scatter(x=time, y=aer_bv, mode='lines', name='Aer. Btura Altura: 28 m.', line=dict(color='#EF553B')))
fig.add_trace(go.Scatter(x=time, y=b_c, mode='lines', name='Bajo Calima Altura: 66 m.', line=dict(color='#00CC96')))
fig.add_trace(go.Scatter(x=time, y=col_pto, mode='lines', name='ColPuertos Altura: 10 m.', line=dict(color='#636EFA')))
fig.add_trace(go.Scatter(x=time, y=la_mis, mode='lines', name='La Misión Altura: 14 m.', line=dict(color='#A569BD')))

fig.update_layout(title = 'Temperatura decadal multianual (1990 - 2023) Estaciones IDEAM',
                  xaxis = dict(title='Años'),
                  yaxis = dict(title='Temperatura (°C)'),
                  title_x = 0.5,
                  template='plotly_white') #'plotly_white' - 'plotly_dark' - 'ggplot2' - 'seaborn - 'simple_white'
fig.show()
'''

''' Parte No 2 
Si queremos agregar varias columnas del DataFrame o Multiples estadisticas a los valores'''
#df1_plus = dato1.groupby(pd.Grouper(key='Fecha', freq='10D')).agg({'ValorMedio': ['mean', 'std'], #Si son varios argumentos los pasamos como un arreglo
                                                              #'ValorMax': 'mean'}).reset_index()# Pasamos las estadisticas como un diccionario y argumento

#print(df1_plus.columns)

#df1_plus.columns = ['_'.join(col) for col in df1_plus]
#print(df1_plus)

#print('Finalizado sin errores')

'''
#Filtering for SP state and price up or equal 115
sp_above_mean = df[(df['price'] >= 115) & (df['seller_state'] == 'SP')]

#Filtering by the quantile - we can remove outliers with this
q1 = df['price'].quantile(0.01)
q2 = df['price'].quantile(0.99)
df_price_outliers = df[(df['price'] >= q1) & (df['price'] <= q2)]

#Creando una nueva columna con apply 
df['price_status'] = df['price'].apply(lambda x: 'UP' if x >= df['price'].mean() else 'DOWN') 
#Creando una nueva columna usando map 
df['seller_by_paid'] = df['paid_type'].map(credit_cards)

#Calculo de estadisticas
df['price'].apply(['min', 'max', 'std', 'median'])

df.apply({
    'price': ['min', 'max', 'std', 'median'],
    'freight_value': ['min', 'max', 'std', 'median', 'mean']
})
'''

#df_enero_multianual = df1_enero.groupby(df1_enero['Fecha'].dt.year)['ValorMedio'].mean()


''' Método no terminado'''
'''Separamos las columnas 'Fecha' y 'ValorMedio' '''
#dato1 = dato1[['Fecha', 'ValorMedio']]

''' Agrupamos por la clave 'fecha' '''
#df2 = dato2.groupby(pd.Grouper(key='Fecha', freq='10D')).mean() #'ME' Mensual
#df1 = dato1.groupby(pd.Grouper(key='Fecha', freq='10D'))['ValorMedio'].mean().reset_index() #'ME' Mensual - 'W' Semanal Inicia Domingo
#df2 = dato2.groupby(pd.Grouper(key='Fecha', freq='ME'))['ValorMedio'].mean().reset_index() #'ME' Mensual
#df3 = dato3.groupby(pd.Grouper(key='Fecha', freq='ME'))['ValorMedio'].mean().reset_index() #'ME' Mensual
#df4 = dato4.groupby(pd.Grouper(key='Fecha', freq='ME'))['ValorMedio'].mean().reset_index() #'ME' Mensual

#print(df1.head())
##print(df2)
##data_frame1 = pd.DataFrame(pd.to_datetime(df1.index), df1['ValorMedio'])
##print(data_frame1['ValorMedio'])

#df1_mes = df1[df1['Fecha'].dt.year==1990]
##df1_enero_2000 = df1_enero[df1_enero['Fecha'].dt.year == 2000]

#print(df1_mes)
##df1_dm = pd.DataFrame(df1_mes)

##df_mul = pd.DataFrame(df_año)
##print(df1_mes.iloc[1::3])
#print(f'Promedio decadal 1: {df1_mes['ValorMedio'].iloc[1::3].mean()}')

#for i in range(1, 13): #iterar desde 1 hasta 12 cada 1
#    df1_mes = df1[df1['Fecha'].dt.month==i]
#    print(f'Mes: {i}')
#    for j in range(1, len(df1_mes)):
#        print(f'Semana: {j}, promedio: {df1_mes['ValorMedio'].iloc[j::3].mean()}')
#print(f'Decadal Enero 2000: {df1_enero_2000['Fecha'][1]}')