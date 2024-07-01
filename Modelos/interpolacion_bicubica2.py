# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:20:03 2024
Aplicando interpolation bicubica a los datos de GCM para escalarlos a 0.1°
@author: Arturo A. Granada G.
"""
import numpy as np
import xarray as xr
from scipy.interpolate import interp2d

r1 = 'Datos/GCM/tas_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca.nc'
r2 = 'Datos/ERA5_Land_T_P/ERA5-Land_2015_2023_ValleDelCauca_3H.nc'

ds1 = xr.open_dataset(r1)
ds2 = xr.open_dataset(r2)

''' Seleccionamos los valores de la variable'''
data_100 = ds1['tas']
data_10 = ds2['t2m']

'''Definir coordenadas a reducir ERA5 Land'''
# Obtenemos las coordenadas originales de los datos GCM
gcm_lon = data_100.coords['lon'].values
gcm_lat = data_100.coords['lat'].values
gcm_values = data_100.values

''' Crear malla de coordenadas para la alta resolución'''
# Coordenadas de la malla objetivo (ERA5)
era5_lon = data_10.coords['longitude'].values
era5_lat = data_10.coords['latitude'].values

''' Crear la función de interpolación bicúbica '''
bicubic_interp = interp2d(gcm_lon, gcm_lat, gcm_values, kind='cubic')

''' Usar la función de interpolación para obtener los valores en la nueva malla '''
interpolated_values = bicubic_interp(era5_lon, era5_lat)

''' Crear un nuevo DataArray con los valores interpolados '''
interpolated_temp = xr.DataArray(interpolated_values, coords=[era5_lat, era5_lon], dims=['latitude', 'longitude'])

'''Exportamos a netCDF'''
interpolated_temp.to_netcdf('tas_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca_11Km_2D.nc')

print('Proceso finalizado')