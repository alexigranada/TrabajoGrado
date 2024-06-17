# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:29:17 2024

Exploración y corte de GCM de precipitación a nivel mundial, para el pacífico Colombiano y cuanca del rio Dagua

@author: Administrator
"""

import pandas as pn
import geopandas as gpn
import xarray as xr
import plotly.graph_objects as go
import rasterio
from rasterio.transform import from_origin
from rasterio.enums import Resampling
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from shapely.geometry import box
import cartopy.crs as ccrs
import numpy as np
import cmocean
import cftime

''' Unión de archivos netCDF'''
#r1 = 'C:/Datos/GCM/CESM2 Ta/ta_day_CESM2-WACCM_historical_r3i1p1f1_gn_20000101-20091231.nc'
#r2 = 'C:/Datos/GCM/CESM2 Tas/tas_day_CESM2_historical_r4i1p1f1_gn_20100101-20150103.nc'
#r3 = 'tas_day_MPI-ESM1-2-HR_historical_r2i1p1f1_gn_20100101-20141231.nc'

#ds1 = xr.open_dataset(r1) #decode_cf=False
#ds2 = xr.open_dataset(r2)
#ds3 = xr.open_dataset(r3)

#result = xr.merge([ds1, ds2], join='outer')
#result.to_netcdf('D:/pr_day_MPI-ESM1-2-HR_historical_r2i1p1f1_gn_20000101-201☺41231.nc')


''' 1. Cargar el conjunto de datos CMIP6 (ejemplo: temperatura media diaria) '''
file = 'Datos/GCM/CESM2 WACCM/tas/tas_day_CESM2-WACCM_ssp245_r3i1p1f1_gn_20150101-20241231_Valle_Cauca.nc'
ds = xr.open_dataset(file)

'''Cargamos los datos de temperatura'''
tas = ds['tas']
print(tas)

'''Promediamos la temperatura'''
tasmean = tas.mean('time', keep_attrs=True)
#print(prmean)
'''Convertimos a °K a °C'''
tasmean.data = tasmean.data - 273.15

'''Cambiamos el argumento a °C '''
tasmean.attrs['units'] = '°C'

''' Cargamos Shapes del Valle y la cuenca '''
geojson_valle = 'Datos/Valle_Cauca_4326.geojson'
geojson_dagua = 'Datos/Cuenca_Dagua_4326.geojson'
gdf_valle = gpn.read_file(geojson_valle)
gdf_dagua = gpn.read_file(geojson_dagua)

''' Ploteamos precipitación nivel mundial '''
#fig = plt.figure(figsize=[24,10], dpi=200)
##ax = fig.add_subplot(222, projection=ccrs.PlateCarree())
#ax = plt.subplot(2, 2, 2, projection=ccrs.PlateCarree())
#tasmean.plot.pcolormesh(ax=ax,
                     ##levels      = np.arange(0, 14, 1),
                     ##extend      = 'max',
                     ##transform   = ccrs.PlateCarree(),
                     ##cbar_kwargs = {'label': tasmean.units},
#                     cmap = 'coolwarm' #'viridis_r'
#                     )
''' Add coast- and gridlines '''
#ax.coastlines(color='black')
#gl = ax.gridlines(draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
#gl.top_labels = False
#gl.right_labels = False
#gdf_valle.boundary.plot(ax=plt.gca(), color='black', linewidth=1, transform=ccrs.PlateCarree())
#gdf_dagua.boundary.plot(ax=plt.gca(), color='black', linewidth=1, transform=ccrs.PlateCarree())
#model = ds.attrs['source_id']
#title = f'[{model}] Temperatura promedio diaria (2000-2014)'
#plt.title(title, fontsize=16, pad=20)
#plt.show()

''' 2. Definir la región de interés mediante coordenadas geográficas (latitud y longitud) '''
#min_lon, max_lon = 270, 300
#min_lat, max_lat = 17, -7

#min_lon_v, max_lon_v = 281, 285
#min_lat_v, max_lat_v = 6, 2

''' 3. Filtrar los datos dentro de la región de interés '''
#ds_roi = ds.sel(lon=slice(min_lon, max_lon), lat=slice(max_lat, min_lat))
#ds_roi_v = ds.sel(lon=slice(min_lon_v, max_lon_v), lat=slice(max_lat_v, min_lat_v))
#print(ds_roi)
''' 5. Guardar el conjunto de datos recortado si es necesario '''
#ds_roi.to_netcdf('Datos/pr_day_CESM2-WACCM_historical_r3i1p1f1_gn_19900101-19991231_Colombia.nc')
#ds_roi_v.to_netcdf('Datos/pr_day_CESM2-WACCM_historical_r3i1p1f1_gn_19900101-19991231_Valle_Cauca.nc')

''' Cargamos Shapes del Valle y la cuenca '''
#geojson_valle = 'C:/Datos/Valle_Cauca_4326.geojson'
#geojson_dagua = 'C:/Datos/Cuenca_Dagua_4326.geojson'
#gdf_valle = gpn.read_file(geojson_valle)
#gdf_dagua = gpn.read_file(geojson_dagua)

''' Promediamos la temperatura '''
#clim = ds_roi['ta'].mean('time', keep_attrs=True)
#clim_v = ds_roi_v['ta'].mean('time', keep_attrs=True)

''' Convertimos °K a °C '''
#clim.data = clim.data - 273.15
#clim.attrs['units'] = '°C'

#clim_v.data = clim_v.data - 273.15
#clim_v.attrs['units'] = '°C' #Cambiamos el argumento a mm/día

#''' Cargamos la precipitación '''
#precipitation_v = ds_roi_v['pr']

#''' Promediamos la precipitación '''
#prmean_v = precipitation_v.mean('time', keep_attrs=True)
#prmean_v.data = prmean_v.data * 86400
#prmean_v.attrs['units'] = 'mm/día'

''' CORTE PARA Pacífico Colombiano '''
''' Ploteamos la temperatura para valle'''
#fig = plt.figure(figsize=[12,5], dpi=100)
#ax = figMean.add_subplot(222, projection=ccrs.PlateCarree(central_longitude=0))
#ax = plt.subplot(2, 2, 2, projection=ccrs.PlateCarree())
#clim.plot.pcolormesh(ax = ax, 
                     #levels = np.arange(0, 14, 1),
                     #extend = 'max', #neither
                     #transform = ccrs.PlateCarree(),
                     #cbar_kwargs = {'label': clim.units},
                     #cmap = 'coolwarm' 
                     #)
''' Add coast- and gridlines '''
#ax.coastlines(color='black')
#gl = ax.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.1, linestyle='--')
#gl.top_labels = False
#gl.right_labels = False
#gdf_valle.boundary.plot(ax=plt.gca(), color='black', linewidth=1, transform=ccrs.PlateCarree())
#gdf_dagua.boundary.plot(ax=plt.gca(), color='black', linewidth=1, transform=ccrs.PlateCarree())
#model = ds.attrs['source_id']
#title = f'[{model}] Temperatura promedio diaria (2000-2014)'
#plt.title(title, fontsize=12, pad=20)
#plt.show()

''' CORTE PARA VALLE '''
''' Ploteamos la Temperatura para valle'''
fig = plt.figure(figsize=[20,10], dpi=200)
#ax = tasmean.add_subplot(222, projection=ccrs.PlateCarree(central_longitude=0))
ax = plt.subplot(projection=ccrs.PlateCarree())
salida = tasmean.plot.pcolormesh(ax = ax, 
                       ##levels = np.arange(0, 14, 1),
                       ##extend = 'max', #neither
                       ##transform = ccrs.PlateCarree(),
                       ##cbar_kwargs = {'label': tasmean.units},
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
gdf_valle.boundary.plot(ax=plt.gca(), color='black', linewidth=1, transform=ccrs.PlateCarree())
gdf_dagua.boundary.plot(ax=plt.gca(), color='black', linewidth=1, transform=ccrs.PlateCarree())

cbar = salida.colorbar
cbar.ax.tick_params(labelsize=16)  # Ajustar el tamaño del texto de la barra de color
#cbar.ax.set_aspect(20)  # Ajustar la proporción de la barra de color (altura vs ancho)
cbar.set_label('Temperatura °C (SSP2-2.5)', fontsize=18, labelpad=20)  # Cambiar la etiqueta de la barra de color

model = ds.attrs['source_id']
title = f'{model} Temperatura promedio diaria (2018-2022)'
plt.title(title, fontsize=30, pad=30, loc='center')
#plt.show()
plt.savefig('Temperatura_GCM.png')
print('completado')