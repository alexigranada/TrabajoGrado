import pandas as pd
import plotly.graph_objects as go
import numpy as np

ruta_e1 = 'Datos/Estaciones/IDEAM/Estaciones Dagua/Temperatura dia/Temperatura_dia_AEROPUERTO BUENAVENTUR [53115010].csv'
ruta_e2 = 'Datos/Estaciones/IDEAM/Estaciones Dagua/Temperatura dia/Temperatura_dia_COLPUERTOS [53115020].csv'
ruta_e3 = 'Datos/Estaciones/IDEAM/Estaciones Dagua/Temperatura dia/Temperatura_dia_BAJO CALIMA [54075020].csv'
ruta_e4 = 'Datos/Estaciones/IDEAM/Estaciones Dagua/Temperatura dia/Temperatura_dia_MISION LA [54075040].csv'

df_e1 = pd.read_csv(ruta_e1, delimiter=';')
df_e2 = pd.read_csv(ruta_e2, delimiter=';')
df_e3 = pd.read_csv(ruta_e3, delimiter=';')
df_e4 = pd.read_csv(ruta_e4, delimiter=';')

''' Creamos el formato de la fecha'''
fechaformato = "%Y-%m-%d"
df_e1['Fecha'] = pd.to_datetime(df_e1['Fecha'], format=fechaformato)
df_e2['Fecha'] = pd.to_datetime(df_e2['Fecha'], format=fechaformato)
df_e3['Fecha'] = pd.to_datetime(df_e3['Fecha'], format=fechaformato)
df_e4['Fecha'] = pd.to_datetime(df_e4['Fecha'], format=fechaformato)

temp_min_e1 = df_e1['ValorMin']#[:50]
temp_min_e2 = df_e2['ValorMin']#[:32]
temp_min_e3 = df_e3['ValorMin']#[:32]
temp_max_e1 = df_e1['ValorMax']#[:50]
temp_max_e2 = df_e2['ValorMax']#[:32]
temp_max_e3 = df_e3['ValorMax']#[:32]
time = df_e1['Fecha']

fig = go.Figure()
fig.add_trace(go.Scatter(x=time, y=temp_max_e1, mode='lines', name='TempMax AER BUENAV ', line=dict(color='#EF553B')))
fig.add_trace(go.Scatter(x=time, y=temp_max_e2, mode='lines', name='TempMax COLPUERTOS', line=dict(color='#636EFA')))
fig.add_trace(go.Scatter(x=time, y=temp_max_e3, mode='lines', name='TempMax B. CALIMA', line=dict(color='#00CC96')))
fig.add_trace(go.Scatter(x=time, y=temp_min_e1, mode='lines', name='TempMin AER BUENAV ', line=dict(color='#EF553B')))
fig.add_trace(go.Scatter(x=time, y=temp_min_e2, mode='lines', name='TempMin COLPUERTOS', line=dict(color='#636EFA')))
fig.add_trace(go.Scatter(x=time, y=temp_min_e3, mode='lines', name='TempMin B. CALIMA', line=dict(color='#00CC96')))

fig.update_layout(title = 'Temperatura estación AERO. BUENAV vs COLPUERTOS',
                  xaxis = dict(title='Años'),
                  yaxis = dict(title='Temperatura (°C)'),
                  title_x = 0.5)
fig.show()

''' Calcula la correlación entre las temperaturas de las dos estaciones meteorológicas '''
correlacion_min_e1_e3 = temp_min_e1.corr(temp_min_e3)
correlacion_max_e1_e3 = temp_max_e1.corr(temp_max_e3)
print('Correlacion Temp. Min E1 vs E3', correlacion_min_e1_e3)
print('Correlacion Temp. Max E1 vs E3', correlacion_max_e1_e3)

''' PARTE Numero 2'''

'''Convermitos TempMin como predictor'''
X = []
temp_min_np = temp_min_e1.to_numpy()
for i in range(len(temp_min_np)):
    row = [[a] for a in temp_min_np[i:i+1]]
    X.append(row)
temp_X = np.array(X)

'''Convertimos TempMax como predictora'''
Y = []
temp_max_np = temp_max_e1.to_numpy()
for i in range(len(temp_max_np)):
    row = temp_max_np[i]
    Y.append(row)
temp_Y = np.array(Y)

'''Dividimos los datos en set de entrenamiento, validacion y prueba'''
X_train, Y_train = temp_X[:40], temp_Y[:40] # 25 valores de entrenamiento
X_val, Y_val     = temp_X[40:45], temp_Y[40:45] # 4 Valores de validación
X_test, Y_test   = temp_X[45:], temp_Y[45:] # 4 valores de prueba

X_train.shape, Y_train.shape, X_val.shape, Y_val.shape, X_test.shape, Y_test.shape