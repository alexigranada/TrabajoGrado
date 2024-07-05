# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:34:30 2024

Exploración variables de ERA5-Land para la cuanca del rio Dagua

@author: Arturo A. Granada G.
"""

import pandas as pn
import geopandas as gpn
import xarray as xr
import plotly.graph_objects as go
from rasterio.transform import from_origin
from rasterio.enums import Resampling
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from shapely.geometry import box
import cartopy.crs as ccrs
import numpy as np
import cmocean
import cftime

ruta = 'Datos/ERA5-Land_2015_2023_ValleDelCauca_3H_Mask.nc'

ds = xr.open_dataset(ruta)
#print(ds)

''' Cargamos las variables '''
precipitacion = ds['tp'][3648:3672] #Seleccionamos las horas del primer año
temperatura = ds['t2m'][:24]

''' Promediamos las variables '''
p_media = precipitacion.sum('time', keep_attrs=True)
t_media = temperatura.mean('time', keep_attrs=True)

''' Cambiamos las unidades de K a C y m a mm '''
#print(t_media)
t_media.data = t_media.data - 273.15
p_media.data = p_media.data / 0.01

print(p_media)
''' Cargamos Shapes del Valle y la cuenca '''
geojson_valle = 'Datos/Valle_Cauca_4326.geojson'
geojson_dagua = 'Datos/Cuenca_Dagua_4326.geojson'
gdf_valle = gpn.read_file(geojson_valle)
gdf_dagua = gpn.read_file(geojson_dagua)

''' Ploteamos la precipitación para la cuenca'''
fig = plt.figure(figsize=[16,10], dpi=200)
#ax = figMean.add_subplot(222, projection=ccrs.PlateCarree(central_longitude=0))
ax = plt.subplot(projection=ccrs.PlateCarree())
salida = p_media.plot.pcolormesh(ax = ax, 
                       levels = np.arange(0, 130, 1),
                       extend = 'neither', #neither - 
                       transform = ccrs.PlateCarree(),
                       cbar_kwargs = {'label': p_media.units},
                       cmap = cmocean.cm.rain 
                       )
''' Add coast- and gridlines '''
ax.coastlines(color='black')
gl = ax.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.4, linestyle='--')
gl.top_labels = False
gl.right_labels = False
gl.xlabel_style = {'size': 16, 'color': 'black'}
gl.ylabel_style = {'size': 16, 'color': 'black'} #'weight': 'bold'

#gdf_valle.boundary.plot(ax=plt.gca(), color='black', linewidth=1, transform=ccrs.PlateCarree())
gdf_dagua.boundary.plot(ax=plt.gca(), color='black', linewidth=1, transform=ccrs.PlateCarree())

cbar = salida.colorbar
cbar.ax.tick_params(labelsize=20)  # Ajustar el tamaño del texto de la barra de color
#cbar.ax.set_aspect(20)  # Ajustar la proporción de la barra de color (altura vs ancho)

''' Reducir el tamaño de la barra de color '''
cbar.ax.set_position([0.77, 0.109, 0.03, 0.77])  # [left, bottom, width, height]
cbar.set_label('Precipitación mm/día', fontsize=24, labelpad=20)  # Cambiar la etiqueta de la barra de color

estaciones = {
    'U. Pacífico': [-76.986, 3.848],
    'La Cumbre': [-76.564, 3.645],
    'Farallones': [-76.6, 3.35],
}

for estacion, (lon, lat) in estaciones.items():
    ax.plot(lon, lat, marker='o', color='red', markersize=6, transform=ccrs.Geodetic())
    ax.text(lon, lat, estacion, transform=ccrs.Geodetic(), fontsize=22, horizontalalignment='center', verticalalignment='bottom',)

#model = ds.attrs['source_id']
title = f'ERA5-Land Precipitación promedio día'
plt.title(title, fontsize=30, pad=30, loc='center')

#plt.show()
plt.savefig('Precipitacion_ERA.png')

''' Ploteamos la Temperatura para valle'''
fig = plt.figure(figsize=[16,10], dpi=200)
#ax = tasmean.add_subplot(222, projection=ccrs.PlateCarree(central_longitude=0))
ax = plt.subplot(projection=ccrs.PlateCarree())
salida = t_media.plot.pcolormesh(ax = ax, 
                       shading='auto',
                       cmap = 'coolwarm' 
                       )
''' Add coast- and gridlines '''
ax.coastlines(color='black')
gl = ax.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.4, linestyle='--')
gl.top_labels = False
gl.right_labels = False
gl.xlabel_style = {'size': 16, 'color': 'black'}
gl.ylabel_style = {'size': 16, 'color': 'black'} #'weight': 'bold'
#gdf_valle.boundary.plot(ax=plt.gca(), color='black', linewidth=1, transform=ccrs.PlateCarree())
gdf_dagua.boundary.plot(ax=plt.gca(), color='black', linewidth=1, transform=ccrs.PlateCarree())

cbar = salida.colorbar
cbar.ax.tick_params(labelsize=20)  # Ajustar el tamaño del texto de la barra de color
#cbar.ax.set_aspect(20)  # Ajustar la proporción de la barra de color (altura vs ancho)
cbar.ax.set_position([0.77, 0.109, 0.03, 0.77])  # [left, bottom, width, height]
cbar.set_label('Temperatura °C', fontsize=24, labelpad=20)  # Cambiar la etiqueta de la barra de color

#model = ds.attrs['source_id']
title = f'ERA5-Land Temperatura promedio día'
plt.title(title, fontsize=30, pad=30, loc='center')
#plt.show()
#plt.savefig('Temperatura_ERA.png')


print('completado')