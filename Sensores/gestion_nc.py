# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 16:58:03 2024

Gestión de datos en formato NetCDF

@author: Arturo A. Granada G.
"""

import xarray as xr
import numpy as np

r = 'Datos/ERA5_Land_T_P/ERA5-Land_2015_2023_ValleDelCauca.nc'
ds = xr.open_dataset(r)

ds_3h = ds.resample(time='3h').mean()

ds_3h.to_netcdf('Datos/ERA5_Land_T_P/ERA5-Land_2015_2023_ValleDelCauca_3H.nc')

print(ds_3h)

print('Proceso Finalizado')