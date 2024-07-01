# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:20:03 2024
Aplicando interpolation bicubica a los datos de GCM para escalarlos a 0.1°
@author: Arturo A. Granada G.
"""
import numpy as np
import xarray as xr
from scipy.ndimage import map_coordinates
from scipy.interpolate import griddata
from scipy.interpolate import interp2d

r1 = 'Datos/GCM/tas_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'
r2 = 'ERA5-Land_2015_2023_ValleDelCauca_3H_Mask.nc'

ds1 = xr.open_dataset(r1)
ds2 = xr.open_dataset(r2)

print(ds2)

''' Seleccionamos los valores de la variable'''
data_100 = ds1['tas']
data_10 = ds2['t2m']

'''Definir coordenadas a reducir ERA5 Land'''
lon_10 = data_10['longitude'].values
lat_10 = data_10['latitude'].values

''' Crear malla de coordenadas para la alta resolución'''
lon_new, lat_new = np.meshgrid(lon_10, lat_10)

dataset_interpolados = []

''' Iteración sobre el Dataset de GCM'''

for fecha in ds1['time'].values:

    ''' Seleccionaos la fecha '''
    #datos_fecha = data_100.sel(time=fecha).values
    datos_fecha = data_100.sel(time=fecha).values

    ''' Definir las coordenadas originales del GCM '''
    lonGCM = ds1['lon'].values
    lon_100 = (lonGCM + 180) % 360 - 180
    lat_100 = ds1['lat'].values

    ''' Crear un grid 2D de coordenadas del GCM '''
    lon_100, lat_100 = np.meshgrid(lon_100, lat_100)

    ''' Aplanar los datos y las coordenadas para la interpolación '''
    puntos = np.array([lon_100.flatten(), lat_100.flatten()]).T
    valores = datos_fecha.flatten()

    datos_interpolados = griddata(puntos, valores, (lon_new, lat_new), method='cubic')

    ds_interpolado = xr.Dataset(
    {
        'tas': (['lat', 'lon'], datos_interpolados)
    },
    coords={
        'lat': (['lat'], ds2['latitude'].values),
        'lon': (['lon'], ds2['longitude'].values)
    }
    )

    dataset_interpolados.append(ds_interpolado)

''' Combinar todos los datasets interpolados en uno solo '''
ds_final = xr.concat(dataset_interpolados, dim='time')
print(ds_final)

''' Exportamos archivo netCDF'''
ds_final.to_netcdf("tas_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca_11Km.nc")

print('Proceso finalizado con exito')