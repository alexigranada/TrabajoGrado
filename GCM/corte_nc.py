# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 16:58:03 2024

Exploración y corte de GCM de variables climatológicas a nivel mundial, para el pacífico Colombiano y cuanca del rio Dagua

@author: Arturo A. Granada G.
"""

import xarray as xr
import numpy as np

r = 'Datos/CESM2 WACCM/VC/hus_day_CESM2-WACCM_ssp245_r3i1p1f1_gn_20150101-20241231.nc'
ds = xr.open_dataset(r)

''' 2. Definir la región de interés mediante coordenadas geográficas (latitud y longitud) '''
min_lon_v, max_lon_v = 281, 285
min_lat_v, max_lat_v = 6, 2

''' 3. Filtrar los datos dentro de la región de interés '''
ds_roi_v = ds.sel(lon=slice(min_lon_v, max_lon_v), lat=slice(max_lat_v, min_lat_v))
print(ds_roi_v)
''' 5. Guardar el conjunto de datos recortado si es necesario '''
ds_roi_v.to_netcdf('Datos/CESM2 WACCM/VC/hus_day_CESM2-WACCM_ssp245_r3i1p1f1_gn_20150101-20241231_ValleDelCauca.nc')

print('Proceso finalizado')
print('Finalizado con exito')