import pandas as pd
import plotly.graph_objects as go

ruta = 'Temperatura_dia_multianual.csv'
data = pd.read_csv(ruta, delimiter=';')

print(data)

data['Fecha'] = pd.to_datetime(data['Fecha'], format='%Y-%m-%d')

tmax = data['ValorMaxMedia'][:365:]
tmin = data['ValorMinMedia'][:365:]
tmedia = (tmax + tmin) / 2
ttime = data['Fecha'][:365:]


fig = go.Figure()
fig.add_trace(go.Scatter(x=ttime, y=tmax, mode='markers', name='Temp. Máx', marker=dict(color='#F44336', size=4)))
fig.add_trace(go.Scatter(x=ttime, y=tmedia, mode='lines', name='Temp. Media', line=dict(color='#8BC34A', width=4)))
fig.add_trace(go.Scatter(x=ttime, y=tmin, mode='markers', name='Temp. Máx', marker=dict(color='#2196F3', size=4)))  

fig.update_layout(title = 'Temperatura diaria multianual (1990 - 2020)',
                  xaxis = dict(title='Años'),
                  yaxis = dict(title='Temperatura (°C)'),
                  title_x = 0.5,
                  template='plotly_white')
fig.show()