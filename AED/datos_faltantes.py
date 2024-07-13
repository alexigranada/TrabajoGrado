# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:29:17 2024

Exploración de datos faltantes

@author: Arturo A. Granada G.
"""
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import geopandas as gpd
from shapely.geometry import Point
import numpy as np

r = 'Datos/ERA5_Land_T_P/ERA5-Land_2015_2023_ValleDelCauca_3H.nc'
ds = xr.open_dataset(r)

gdf = gpd.read_file('Datos/Mascara.geojson')
polygon = gdf.geometry[0]
# Crear una máscara basada en el polígono
lats = ds.latitude.values
lons = ds.longitude.values

t = ds['t2m']

# Inicializar la máscara como un array de True
mask = np.ones((len(lats), len(lons)), dtype=bool)

# Convertir las coordenadas de latitud y longitud a puntos y verificar si están dentro del polígono
for i, lat in enumerate(lats):
    for j, lon in enumerate(lons):
        point = Point(lon, lat)
        if polygon.contains(point):
            mask[i, j] = True

# Aplicar la máscara a las variables de interés
masked_ds = t.where(mask)

print(masked_ds)
#masked_ds.to_netcdf('era5-land-masked.nc')
#temperatura = ds['t2m']
#nulos = temperatura.isnull()
#print(nulos)
'''
for variable in ds.variables:
    faltantes = ds[variable].isnull().sum()
    print(f'Datos faltantes variable {variable}: {faltantes}')


# Escoger un paso de tiempo, por ejemplo el primero
sample_time_slice = ds['t2m'].isel(time=1)

# Crear una máscara de datos faltantes
missing_mask = sample_time_slice.isnull()

fig = plt.figure(figsize=(10, 5))
ax = plt.axes(projection=ccrs.PlateCarree())

# Graficar la máscara de datos faltantes
missing_mask.plot(ax=ax, transform=ccrs.PlateCarree(), add_colorbar=False, cmap='coolwarm')

ax.coastlines()
plt.title('Distribución de Datos Faltantes para t2m en un Paso de Tiempo')
plt.show()
'''