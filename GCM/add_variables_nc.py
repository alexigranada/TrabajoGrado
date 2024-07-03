# -*- coding: utf-8 -*-
"""
Created on Wed Jul 1 07:50:33 2024

Añadir variables a archivos NetCDF

@author: Arturo A. Granada G.
"""
import xarray as xr
import rioxarray

r1 = 'tas_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca_ERA.nc'
r2 = 'Datos/DEM_RE_ERA_FINAL.tif'

ds1 = xr.open_dataset(r1)
ds2 = rioxarray.open_rasterio(r2)

print(ds2)

'''Seleccionamos los valores de altura en cada pixel del DEM'''
altitud_con_coordenadas = xr.DataArray(data=ds2.values.squeeze(), 
                                       dims=["lat", "lon"],
                                       coords={"lat": ds1.coords["lat"], "lon": ds1.coords["lon"]})
#print(altura)

ds1['h'] = altitud_con_coordenadas
ds1['h'].attrs['units'] = 'metros (m)'
ds1['h'].attrs['description'] = 'm.s.n.m (ALOS-PALSAR)'

print(ds1)

ds1.to_netcdf('tas_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca_11Km_Mask_h.nc')