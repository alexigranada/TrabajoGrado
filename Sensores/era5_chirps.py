# -*- coding: utf-8 -*-
"""
Created on Fri May 31 21:11:20 2024

Correlacion entre datos de precipitación ERA5-Land y CHIRPS

@author: Arturo A. Granada G.
"""
import xarray as xr
import pandas as pd
import plotly.graph_objects as go


rch = 'Datos/CHIRPS/Dagua.nc'
rera = 'Datos/ERA5/ERA5-Land_17-22.nc'

ds_ch = xr.open_dataset(rch)
ds_era = xr.open_dataset(rera)

#print(ds_ch)
print(ds_ch['Y'])
print(ds_ch['X'])


