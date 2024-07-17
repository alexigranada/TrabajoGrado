# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:33:48 2024
Exploración de las estaciones del IDEAM y DEM alosparlsar a 0.1°
@author: Arturo A. Granada g.
"""
import rioxarray
import xarray as xr
import geopandas as gpn
from rasterio.transform import from_origin
from rasterio.enums import Resampling
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from shapely.geometry import box
import cartopy.crs as ccrs
import numpy as np
import cmocean

ruta = 'Datos/DEM_RE_ERA_FINAL.tif'

ds = rioxarray.open_rasterio(ruta)
dem = ds.sel(band=1)
#print(dem)

''' Cargamos Shapes del Valle y la cuenca '''
geojson_valle = 'Datos/Valle_Cauca_4326.geojson'
geojson_dagua = 'Datos/Cuenca_Dagua_4326.geojson'
gdf_valle = gpn.read_file(geojson_valle)
gdf_dagua = gpn.read_file(geojson_dagua)

''' Agregar estaciones al mapa (Puntos) '''
estaciones = {
    'U. Pacífico': [-76.9869, 3.8480],
    'La Cumbre': [-76.5647, 3.6451],
    'Farallones': [-76.6513, 3.4158],
    'Univalle': [-76.5338, 3.3777],
    'Siloe': [-76.5605, 3.4252],
    'Aero. A. Bonilla': [-76.3822, 3.5327],
    'La Diana': [-76.1855, 3.3138]
}



fig = plt.figure(figsize=[24,15], dpi=400)
#ax = figMean.add_subplot(222, projection=ccrs.PlateCarree(central_longitude=0))
ax = plt.subplot(projection=ccrs.PlateCarree())
salida = dem.plot.pcolormesh(ax = ax, 
                       #levels = np.arange(0, 4000, 100),
                       #extend = 'neither', #max
                       transform = ccrs.PlateCarree(),
                       cbar_kwargs = {'label': 'Elevación (m)'},
                       cmap = cmocean.cm.dense 
                       )
''' Establecer los límites geográficos [lon_min, lon_max, lat_min, lat_max] '''
ax.set_extent([-77.6, -76.0, 3.0, 4.3])

''' Add coast- and gridlines '''
#ax.coastlines(color='black')
gl = ax.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.4, linestyle='--')
gl.top_labels = False
gl.right_labels = False
gl.xlabel_style = {'size': 18, 'color': 'black'}
gl.ylabel_style = {'size': 18, 'color': 'black'} #'weight': 'bold'

gdf_valle.boundary.plot(ax=plt.gca(), color='black', linewidth=1, transform=ccrs.PlateCarree())
gdf_dagua.boundary.plot(ax=plt.gca(), color='black', linewidth=1, transform=ccrs.PlateCarree())


ax.plot(-76.9869, 3.8480, marker='o', color='red', markersize=8, transform=ccrs.Geodetic())
ax.text(-76.9869, 3.8480 + 0.07, 'Unipacífico', transform=ccrs.Geodetic(), fontsize=18, horizontalalignment='center', verticalalignment='top', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

ax.plot(-76.5647, 3.6451, marker='o', color='red', markersize=8, transform=ccrs.Geodetic())
ax.text(-76.5647, 3.6451 + 0.07, 'La Cumbre', transform=ccrs.Geodetic(), fontsize=18, horizontalalignment='center', verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

ax.plot(-76.6513, 3.4158, marker='o', color='red', markersize=8, transform=ccrs.Geodetic())
ax.text(-76.6513 - 0.05, 3.4158, 'Farallones', transform=ccrs.Geodetic(), fontsize=18, horizontalalignment='right', verticalalignment='center', bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

ax.plot(-76.5338, 3.3777, marker='o', color='red', markersize=8, transform=ccrs.Geodetic())
ax.text(-76.5338, 3.3777 - 0.07, 'Univalle', transform=ccrs.Geodetic(), fontsize=18, horizontalalignment='center', verticalalignment='bottom', bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

ax.plot(-76.5605, 3.4252, marker='o', color='red', markersize=8, transform=ccrs.Geodetic())
ax.text(-76.5605, 3.4252 + 0.07, 'Siloe', transform=ccrs.Geodetic(), fontsize=18, horizontalalignment='center', verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

ax.plot(-76.1855, 3.3138, marker='o', color='red', markersize=8, transform=ccrs.Geodetic())
ax.text(-76.1855, 3.3138 + 0.07, 'La Diana', transform=ccrs.Geodetic(), fontsize=18, horizontalalignment='center', verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

ax.plot(-76.3822, 3.5327, marker='o', color='red', markersize=8, transform=ccrs.Geodetic())
ax.text(-76.3822 + 0.17, 3.5327, 'Arpto A. Bonilla', transform=ccrs.Geodetic(), fontsize=18, horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

cbar = salida.colorbar
cbar.ax.tick_params(labelsize=16)  # Ajustar el tamaño del texto de la barra de color
#cbar.ax.set_aspect(20)  # Ajustar la proporción de la barra de color (altura vs ancho)
cbar.set_label('Elevación (m)', fontsize=18, labelpad=20)  # Cambiar la etiqueta de la barra de color

#model = ds.attrs['source_id']
title = f'Distribución de las estaciones locales'
plt.title(title, fontsize=35, pad=30, loc='center')

#plt.show()
plt.savefig('Estaciones_DEM.png')
print('completado')