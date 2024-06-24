# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 16:58:03 2024

Exploración y corte de GCM de variables climatológicas a nivel mundial, para el pacífico Colombiano y cuanca del rio Dagua

@author: Arturo A. Granada G.
"""

import xarray as xr
import numpy as np

r = 'Datos/ERA5_Land_T_P/ERA5-Land_2015_2023.nc'
ds = xr.open_dataset(r)
print(ds.coords)

''' 2. Definir la región de interés mediante coordenadas geográficas (latitud y longitud) '''
min_lon_v, max_lon_v = -77.7, -76
min_lat_v, max_lat_v = 3, 4.3

''' 3. Filtrar los datos dentro de la región de interés '''
ds_roi_v = ds.sel(longitude=slice(min_lon_v, max_lon_v), latitude=slice(max_lat_v, min_lat_v))
print(ds_roi_v)

''' 5. Guardar el conjunto de datos recortado si es necesario '''
ds_roi_v.to_netcdf('Datos/ERA5_Land_T_P/ERA5-Land_2015_2023_ValleDelCauca.nc')

print('Proceso finalizado')
print('Finalizado con exito')