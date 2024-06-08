# -*- coding: utf-8 -*-
"""
Created on Sun May 29 07:49:49 2024

Exploración de datos de precipitación de ERA5-Land, CHIRPS y Datos de estaciones

@author: Arturo A. Granada G.
"""

'''Importamos librerias'''
import pandas as pd #Leer datos
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt #Graficas para datos

#era = 'Datos/CorrelacionPrecipitacion/Pacifico/ERAPacifico.csv'
#ch1 = 'Datos/CorrelacionPrecipitacion/Pacifico/CH1Pacifico.csv' #Ruta del archivo CHIRPS
#ch2 = 'Datos/CorrelacionPrecipitacion/Pacifico/CH2Pacifico.csv'
#ch3 = 'Datos/CorrelacionPrecipitacion/Pacifico/CH3Pacifico.csv'
#ch4 = 'Datos/CorrelacionPrecipitacion/Pacifico/CH4Pacifico.csv'
#ch5 = 'Datos/CorrelacionPrecipitacion/Pacifico/CH5Pacifico.csv'

#era = 'Datos/CorrelacionPrecipitacion/LaCumbre/ERALaCumbre.csv'
#ch1 = 'Datos/CorrelacionPrecipitacion/LaCumbre/CH1Cumbre.csv' #Ruta del archivo CHIRPS
#ch2 = 'Datos/CorrelacionPrecipitacion/LaCumbre/CH2Cumbre.csv'
#ch3 = 'Datos/CorrelacionPrecipitacion/LaCumbre/CH3Cumbre.csv'
#ch4 = 'Datos/CorrelacionPrecipitacion/LaCumbre/CH4Cumbre.csv'

era = 'Datos/CorrelacionPrecipitacion/Farallones/ERAFarallones.csv'
ch1 = 'Datos/CorrelacionPrecipitacion/Farallones/CH1Farallones.csv' #Ruta del archivo CHIRPS
#ch2 = 'Datos/CorrelacionPrecipitacion/Farallones/CH2Farallones.csv'

df_era = pd.read_csv(era, delimiter=',', index_col='Fecha',  parse_dates=['Fecha'])
df_ch1 = pd.read_csv(ch1, delimiter=',', index_col='Fecha',  parse_dates=['Fecha'])
#df_ch2 = pd.read_csv(ch2, delimiter=',', index_col='Fecha',  parse_dates=['Fecha'])
#df_ch3 = pd.read_csv(ch3, delimiter=',', index_col='Fecha',  parse_dates=['Fecha'])
#df_ch4 = pd.read_csv(ch4, delimiter=',', index_col='Fecha',  parse_dates=['Fecha'])
#df_ch5 = pd.read_csv(ch5, delimiter=',', index_col='Fecha',  parse_dates=['Fecha'])

#df = df.dropna()
'''Convertimos datos ERA a día'''
era_dia = df_era.resample('D').sum()
#print(era_dia)
#print(df_ch1)

'''Convertimos datos ERA y CHIRPS a semanal'''
era_sem = df_era.resample('W').sum()
ch_sem = df_ch1.resample('W').sum()

'''Convertimos datos ERA y CHIRPS a Mensual'''
era_mes = df_era.resample('ME').sum()
ch_mes = df_ch1.resample('ME').sum()

'''Datos día'''
#estacion = df_dia['Precipitacion'][:90]

era5 = era_dia['P1']#[:90] --CAMBIAR--
chirps1 = df_ch1['P_1_1']#[:90]df_ch3
chirps2 = df_ch1['P_1_2']
chirps3 = df_ch1['P_1_3']
chirps4 = df_ch1['P_1_4']

#era5 = era_sem['P4']
#chirps1 = ch_sem['P_4_1']#[:90]df_ch3
#chirps2 = ch_sem['P_4_2']
#chirps3 = ch_sem['P_4_3']
#chirps4 = ch_sem['P_4_4']

#era5 = era_mes['P4']
#chirps1 = ch_mes['P_4_1']#[:90]df_ch3
#chirps2 = ch_mes['P_4_2']
#chirps3 = ch_mes['P_4_3']
#chirps4 = ch_mes['P_4_4']

#time = era_mes.index

#fig = go.Figure()

#fig.add_trace(go.Bar(x=time, y=era5, name='ERA5', marker_color='#EF553B'))#Rojo
#fig.add_trace(go.Bar(x=time, y=chirps1, name='CHIRPS P1', marker_color='#636EFA'))#Azul
#fig.add_trace(go.Bar(x=time, y=chirps2, name='CHIRPS P2', marker_color='#636EFA'))#Morado
#fig.add_trace(go.Bar(x=time, y=chirps3, name='CHIRPS P3', marker_color='#636EFA'))#Morado
#fig.add_trace(go.Bar(x=time, y=chirps4, name='CHIRPS P4', marker_color='#636EFA'))#Morado

#title = f'Precipitación ERA5 vs CHRIPS - Zona Pacífico'
#fig.update_layout(title = title,
#                  title_font_size=22,
#                  xaxis = dict(title='Tiempo (Mes)'),
#                  yaxis = dict(title='Precipitación (mm/mes)'),
#                  template = 'seaborn',
#                  title_x = 0.5)
#fig.show()
#fig.write_image("Precipitacion_Mes_Pacifico_ERA_CHIRPS.png", width=800, height=500, scale=4)

correlacion_Era1 = chirps1.corr(era5)
correlacion_Era2 = chirps2.corr(era5)
correlacion_Era3 = chirps3.corr(era5)
correlacion_Era4 = chirps4.corr(era5)

print('Correlacion precipitacion ERA5 vs CHIRPS 1: ', correlacion_Era1)
print('Correlacion precipitacion ERA5 vs CHIRPS 2: ', correlacion_Era2)
print('Correlacion precipitacion ERA5 vs CHIRPS 3: ', correlacion_Era3)
print('Correlacion precipitacion ERA5 vs CHIRPS 4: ', correlacion_Era4)

''' PRECIPITACIÓN SEMANAL'''
#df_semana = df.resample('W').sum()
#print(df_semana)

#estacion2 = df_semana['PrecipitacionT']
#era52 = df_semana['total_precipitation']
#time2 = df_semana.index

#fig2 = go.Figure()

#fig2.add_trace(go.Bar(x=time2, y=estacion2, name='EstaciónT', marker_color='#636EFA'))#Morado
#fig2.add_trace(go.Bar(x=time2, y=era52, name='ERA5', marker_color='#EF553B'))#Rojo

#title2 = f'Precipitación ERA5 y Estación U. Pacífico'
#fig2.update_layout(title = title2,
#                  title_font_size=22,
#                  xaxis = dict(title='Semana'),
#                  yaxis = dict(title='Precipitación (mm/semanal)'),
#                  template = 'seaborn',
#                  title_x = 0.5)
#fig2.show()
#fig2.write_image("PrecipitacionT_semana_era5_UP.png", width=800, height=500, scale=4)


'''PRECIPITACIÓN MENS'''

#df_mes = df.resample('ME').sum()
#print(df_mes)

#estacion3 = df_mes['PrecipitacionT']
#era53 = df_mes['total_precipitation']
#time3 = df_mes.index

#fig3 = go.Figure()

#fig3.add_trace(go.Bar(x=time3, y=estacion3, name='EstaciónT', marker_color='#636EFA'))#Morado
#fig3.add_trace(go.Bar(x=time3, y=era53, name='ERA5', marker_color='#EF553B'))#Rojo

#title3 = f'Precipitación ERA5 y Estación U. Pacífico'
#fig3.update_layout(title = title,
#                  title_font_size=22,
#                  xaxis = dict(title='Mes'),
#                  yaxis = dict(title='Precipitación (mm/mes)'),
#                  template = 'seaborn',
#                  title_x = 0.5)
#fig3.show()
#fig3.write_image("PrecipitacionT_mes_era5_UP.png", width=800, height=500, scale=4)