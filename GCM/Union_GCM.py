import xarray as xr

''' Unión de archivos netCDF'''
#r1 = 'C:/Datos/GCM/CESM2 WACCM/Pr/pr_day_CESM2-WACCM_historical_r3i1p1f1_gn_20000101-20091231.nc'
#r2 = 'C:/Datos/GCM/CESM2 WACCM/Pr/pr_day_CESM2-WACCM_historical_r3i1p1f1_gn_20100101-20150101.nc'
#r3 = 'C:/Datos/GCM/CESM2 Pr/pr_day_CESM2_ssp245_r4i1p1f1_gn_20350101-20441231.nc'
#r4 = 'C:/Datos/GCM/CESM2 Pr/pr_day_CESM2_ssp245_r4i1p1f1_gn_20450101-20541231.nc'
#r5 = 'C:/Datos/GCM/CESM2 Pr/pr_day_CESM2_ssp245_r4i1p1f1_gn_20550101-20641231.nc'
#r6 = 'C:/Datos/GCM/CESM2 Pr/pr_day_CESM2_ssp245_r4i1p1f1_gn_20650101-20741231.nc'
#r7 = 'C:/Datos/GCM/CESM2 Pr/pr_day_CESM2_ssp245_r4i1p1f1_gn_20750101-20841231.nc'
#r8 = 'C:/Datos/GCM/CESM2 Pr/pr_day_CESM2_ssp245_r4i1p1f1_gn_20850101-20941231.nc'
#r9 = 'C:/Datos/GCM/CESM2 Pr/pr_day_CESM2_ssp245_r4i1p1f1_gn_20950101-21010101.nc'
#r1 = 'Datos/ERA5/ERA5/era5_012022.nc'
#r2 = 'Datos/ERA5/ERA5/era5_022022.nc'
#r3 = 'Datos/ERA5/ERA5/era5_032022.nc'
#r4 = 'Datos/ERA5/ERA5/era5_042022.nc'
#r5 = 'Datos/ERA5/ERA5/era5_052022.nc'
#r6 = 'Datos/ERA5/ERA5/era5_062022.nc'
#r7 = 'Datos/ERA5/ERA5/era5_072022.nc'
#r8 = 'Datos/ERA5/ERA5/era5_082022.nc'
#r9 = 'Datos/ERA5/ERA5/era5_092022.nc'
#r10 = 'Datos/ERA5/ERA5/era5_102022.nc'
#r11 = 'Datos/ERA5/ERA5/era5_112022.nc'
#r12 = 'Datos/ERA5/ERA5/era5_122022.nc'
r1 = 'Datos/ERA5/ERA5-Land_2017.nc'
r2 = 'Datos/ERA5/ERA5-Land_2018.nc'
r3 = 'Datos/ERA5/ERA5-Land_2019.nc'
r4 = 'Datos/ERA5/ERA5-Land_2020.nc'
r5 = 'Datos/ERA5/ERA5-Land_2021.nc'
r6 = 'Datos/ERA5/ERA5-Land_2022.nc'

ds1 = xr.open_dataset(r1) #decode_cf=False
ds2 = xr.open_dataset(r2)
ds3 = xr.open_dataset(r3)
ds4 = xr.open_dataset(r4) #decode_cf=False
ds5 = xr.open_dataset(r5)
ds6 = xr.open_dataset(r6)
#ds7 = xr.open_dataset(r7) #decode_cf=False
#ds8 = xr.open_dataset(r8)
#ds9 = xr.open_dataset(r9)
#ds10 = xr.open_dataset(r10)
#ds11 = xr.open_dataset(r11)
#ds12 = xr.open_dataset(r12)

result = xr.merge([ds1, ds2, ds3, ds4, ds5, ds6], join='outer') #, ds3, ds4, ds5, ds6, ds7, ds8, ds9, ds10, ds11, ds12
result.to_netcdf('Datos/ERA5/ERA5-Land_17-22.nc')
print('Unión completada')