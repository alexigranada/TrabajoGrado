'''

[desde:hasta:pasoDeTiempo]

'''

import pandas as pd
import plotly.graph_objects as go

r = 'Datos/Estaciones/IDEAM/Estaciones Dagua/Temperatura_dia_multianual.csv'
r1 = 'Datos/Estaciones/IDEAM/Estaciones Dagua/Temperatura dia/Temperatura_dia_BAJO CALIMA [54075020].csv'
r2 = 'Datos/Estaciones/IDEAM/Estaciones Dagua/Temperatura dia/Temperatura_dia_COLPUERTOS [53115020].csv'
#r3 = 'Datos/Datos_Hidrometeorol_gicos_Crudos_-_Red_de_Estaciones_IDEAM___Temperatura_20240412.csv'
data = pd.read_csv(r, delimiter=';')
data1 = pd.read_csv(r1, delimiter=';')
data2 = pd.read_csv(r2, delimiter=';')
print(data)

data['Fecha'] = pd.to_datetime(data['Fecha'], format='%Y-%m-%d')
data1['Fecha'] = pd.to_datetime(data1['Fecha'], format='%Y-%m-%d')
data2['Fecha'] = pd.to_datetime(data2['Fecha'], format='%Y-%m-%d')

#print(data['Valor'])
#print(data['Fecha'])
tmax = data['ValorMaxMedia'][:1461:]
tmin = data['ValorMinMedia'][:1461:]

tmax1 = data1['ValorMax'][:1461:]
tmin1 = data1['ValorMin'][:1461:]

tmax2 = data2['ValorMax'][:1461:]
tmin2 = data2['ValorMin'][:1461:]
#tmedia = (tmax + tmin) / 2
ttime = data['Fecha'][:1461:]


fig = go.Figure()
fig.add_trace(go.Scatter(x=ttime, y=tmax, mode='markers', name='Temp. DMA Máx', marker=dict(color='red', size=4)))
fig.add_trace(go.Scatter(x=ttime, y=tmin, mode='markers', name='Temp. DMA Mín', marker=dict(color='red', size=4)))
fig.add_trace(go.Scatter(x=ttime, y=tmax1, mode='lines', name='Temp. Máx', line=dict(color='#FF9800')))
fig.add_trace(go.Scatter(x=ttime, y=tmin1, mode='lines', name='Temp. Mín', line=dict(color='#FF9800'))) 
fig.add_trace(go.Scatter(x=ttime, y=tmax2, mode='lines', name='Temp. Máx', line=dict(color='#2196F3')))
fig.add_trace(go.Scatter(x=ttime, y=tmin2, mode='lines', name='Temp. Mín', line=dict(color='#2196F3')))
   

fig.update_layout(title = 'Temperatura diaria multianual (1990 - 2020)',
                  xaxis = dict(title='Años'),
                  yaxis = dict(title='Temperatura (°C)'),
                  title_x = 0.5,
                  template='plotly_white')
fig.show()

print(tmax1)
''' Reemplazamos los valores nulos por los valores calculados'''
data1.loc[:1461:, 'ValorMax'] = data1.loc[:1461:, 'ValorMax'].fillna(data['ValorMaxMedia'])
data2.loc[:1461:, 'ValorMax'] = data2.loc[:1461:, 'ValorMax'].fillna(data['ValorMaxMedia'])

data1.loc[:1461:, 'ValorMin'] = data1.loc[:1461:, 'ValorMin'].fillna(data['ValorMinMedia'])
data2.loc[:1461:, 'ValorMin'] = data2.loc[:1461:, 'ValorMin'].fillna(data['ValorMinMedia'])

tmax = data['ValorMaxMedia'][:1461:]
tmin = data['ValorMinMedia'][:1461:]

tmax1 = data1['ValorMax'][:1461:]
tmin1 = data1['ValorMin'][:1461:]

tmax2 = data2['ValorMax'][:1461:]
tmin2 = data2['ValorMin'][:1461:]
#tmedia = (tmax + tmin) / 2
ttime = data['Fecha'][:1461:]

fig = go.Figure()
fig.add_trace(go.Scatter(x=ttime, y=tmax, mode='markers', name='Temp. DMA Máx', marker=dict(color='red', size=4)))
fig.add_trace(go.Scatter(x=ttime, y=tmin, mode='markers', name='Temp. DMA Mín', marker=dict(color='red', size=4)))
fig.add_trace(go.Scatter(x=ttime, y=tmax1, mode='lines', name='Temp. Máx', line=dict(color='#FF9800')))
fig.add_trace(go.Scatter(x=ttime, y=tmin1, mode='lines', name='Temp. Mín', line=dict(color='#FF9800'))) 
fig.add_trace(go.Scatter(x=ttime, y=tmax2, mode='lines', name='Temp. Máx', line=dict(color='#2196F3')))
fig.add_trace(go.Scatter(x=ttime, y=tmin2, mode='lines', name='Temp. Mín', line=dict(color='#2196F3')))
   

fig.update_layout(title = 'Temperatura diaria multianual (1990 - 2020)',
                  xaxis = dict(title='Años'),
                  yaxis = dict(title='Temperatura (°C)'),
                  title_x = 0.5,
                  template='plotly_white')
fig.show()

print('Finalizado con exito')