# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:34:30 2024

Exploración y corte de GCM de precipitación a nivel mundial, para el pacífico Colombiano y cuanca del rio Dagua

@author: Arturo A. Granada G.
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
#r1 = 'C:/Datos/GCM/CESM2 Pr/pr_day_CESM2_historical_r4i1p1f1_gn_20000101-20091231.nc'
#r2 = 'C:/Datos/GCM/CESM2 Pr/pr_day_CESM2_historical_r4i1p1f1_gn_20100101-20150103.nc'
#r3 = 'C:/Users/Administrator/Downloads/Pricipitation/pr_day_MPI-ESM1-2-HR_historical_r2i1p1f1_gn_20100101-20141231.nc'

#ds1 = xr.open_dataset(r1) #decode_cf=False
#ds2 = xr.open_dataset(r2)
#ds3 = xr.open_dataset(r3)

#result = xr.merge([ds1, ds2], join='outer')
#result.to_netcdf('C:/Datos/GCM/CESM2 Pr/pr_day_CESM2_historical_r4i1p1f1_gn_20000101-20150103.nc')


''' 1. Cargar el conjunto de datos CMIP6 (ejemplo: temperatura media diaria) '''
file = 'Datos/GCM/CESM2 WACCM/pr/pr_day_CESM2-WACCM_ssp245_r3i1p1f1_gn_20150101-20241231_Valle_Cauca.nc'
ds = xr.open_dataset(file)

''' Cargamos los datos de precipitación '''
prec = ds['pr']
#print(prec)

''' Promediamos la precipitación '''
prmean = prec.mean('time', keep_attrs=True)
#print(prmean)
''' Convertimos a mm/día '''
prmean.data = prmean.data * 86400

''' Cambiamos el argumento a mm/día '''
prmean.attrs['units'] = 'mm/day'

''' Ploteamos precipitación nivel mundial '''
#fig = plt.figure(figsize=[24,10], dpi=200)
#ax = fig.add_subplot(222, projection=ccrs.PlateCarree())
#prmean.plot.contourf(ax=ax,
                     #levels      = np.arange(0, 14, 1),
                     #extend      = 'max',
                     #transform   = ccrs.PlateCarree(),
                     #cbar_kwargs = {'label': prmean.units},
                     #cmap = cmocean.cm.rain #'viridis_r'
                     #)
''' Add coast- and gridlines '''
#ax.coastlines(color='black')
#gl = ax.gridlines(draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
#gl.top_labels = False
#gl.right_labels = False
#gdf_valle.boundary.plot(ax=plt.gca(), color='black', linewidth=1, transform=ccrs.PlateCarree())
#gdf_dagua.boundary.plot(ax=plt.gca(), color='black', linewidth=1, transform=ccrs.PlateCarree())
#model = ds.attrs['source_id']
#title = f'[{model}] Precipitación promedio diaria (2000-2014)'
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
#ds_roi.to_netcdf('C:/Datos/GCM/CESM2 Pr/pr_day_CESM2_ssp585_r4i1p1f1_gn_20950101-21010101_Colombia.nc')
#ds_roi_v.to_netcdf('C:/Datos/GCM/CESM2 Pr/pr_day_CESM2_ssp585_r4i1p1f1_gn_20950101-21010101_Valle_Cauca.nc')

''' Cargamos Shapes del Valle y la cuenca '''
geojson_valle = 'Datos/Valle_Cauca_4326.geojson'
geojson_dagua = 'Datos/Cuenca_Dagua_4326.geojson'
gdf_valle = gpn.read_file(geojson_valle)
gdf_dagua = gpn.read_file(geojson_dagua)

''' Promediamos la precipitación '''
#clim = ds_roi['pr'].mean('time', keep_attrs=True)
#clim_v = ds_roi_v['pr'].mean('time', keep_attrs=True)

''' Convertimos Kg/m2/s a mm/día ''' 
#clim.data = clim.data * 86400
#clim.attrs['units'] = 'mm/day'

#clim_v.data = clim_v.data * 86400
#clim_v.attrs['units'] = 'mm/day' #Cambiamos el argumento a mm/día

#''' Cargamos la precipitación '''
#precipitation_v = ds_roi_v['pr']

#''' Promediamos la precipitación '''
#prmean_v = precipitation_v.mean('time', keep_attrs=True)
#prmean_v.data = prmean_v.data * 86400
#prmean_v.attrs['units'] = 'mm/día'

''' Corte para Pacífico Colombiano '''
''' Ploteamos la precipitación para valle'''
#fig = plt.figure(figsize=[24,10], dpi=200)
#ax = figMean.add_subplot(222, projection=ccrs.PlateCarree(central_longitude=0))
#ax = plt.subplot(2, 2, 2, projection=ccrs.PlateCarree())
#clim.plot.pcolormesh(ax = ax, 
#                     levels = np.arange(0, 14, 1),
#                     extend = 'max', #neither
#                     transform = ccrs.PlateCarree(),
#                     cbar_kwargs = {'label': clim.units},
#                     cmap = cmocean.cm.rain 
#                     )
''' Add coast- and gridlines '''
#ax.coastlines(color='black')
#gl = ax.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.1, linestyle='--')
#gl.top_labels = False
#gl.right_labels = False
#gdf_valle.boundary.plot(ax=plt.gca(), color='black', linewidth=1, transform=ccrs.PlateCarree())
#gdf_dagua.boundary.plot(ax=plt.gca(), color='black', linewidth=1, transform=ccrs.PlateCarree())
#model = ds.attrs['source_id']
#title = f'[{model}] Precipitación promedio diaria (2000-2014)'
#plt.title(title, fontsize=12, pad=20)
#plt.show()

''' CORTE PARA VALLE '''
''' Ploteamos la precipitación para valle'''
fig = plt.figure(figsize=[16,10], dpi=200)
#ax = figMean.add_subplot(222, projection=ccrs.PlateCarree(central_longitude=0))
ax = plt.subplot(projection=ccrs.PlateCarree())
salida = prmean.plot.pcolormesh(ax = ax, 
                       levels = np.arange(0, 14, 1),
                       extend = 'max', #neither
                       transform = ccrs.PlateCarree(),
                       cbar_kwargs = {'label': prmean.units},
                       cmap = cmocean.cm.rain 
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
cbar.set_label('Precipitación mm/día (SSP2-2.5)', fontsize=18, labelpad=20)  # Cambiar la etiqueta de la barra de color

model = ds.attrs['source_id']
title = f'{model} Precipitación promedio diaria (2018-2022)'
plt.title(title, fontsize=30, pad=30, loc='center')

#plt.show()
plt.savefig('Precipitacion_GCM.png')
print('completado')