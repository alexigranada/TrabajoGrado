# -*- coding: utf-8 -*-
"""
Created on Wed Jul 1 07:50:33 2024

Añadir variables a archivos NetCDF

@author: Arturo A. Granada G.
"""
import xarray as xr

r1 = 'Datos/'
r2 = 'Datos/'

ds1 = xr.open_dataset(r1)
ds2 = xr.open_dataset(r2)