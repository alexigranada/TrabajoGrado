# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 16:58:03 2024

Exploración y corte de GCM de variables climatológicas a nivel mundial, para el pacífico Colombiano y cuanca del rio Dagua

@author: Arturo A. Granada G.
"""

import xarray as xr
import numpy as np

r = 'Datos/vas_3hr_GFDL-ESM4_ssp119_r1i1p1f1_gr1_201501010300-203501010000.nc'
ds = xr.open_dataset(r)
print(ds['lon'].values)

''' 2. Definir la región de interés mediante coordenadas geográficas (latitud y longitud) '''
''' Para GCM Valle lon: 281-285 lat: 2-6'''
min_lon_v, max_lon_v = 281.875, 284.375
min_lat_v, max_lat_v = 2.5, 5.5

''' 3. Filtrar los datos dentro de la región de interés '''
ds_roi_v = ds.sel(lon=slice(min_lon_v, max_lon_v), lat=slice(min_lat_v, max_lat_v))
print(ds_roi_v)

''' 5. Guardar el conjunto de datos recortado si es necesario '''
#ds_roi_v.to_netcdf('Datos/vas_3hr_GFDL-ESM4_ssp119_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc')

print('Proceso finalizado')
print('Finalizado con exito')