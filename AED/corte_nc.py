

import matplotlib.pyplot as plt
import rioxarray
import xarray as xr
import geopandas as gpd
from shapely.geometry import mapping

r = 'Datos/GFDL SSP 126 Valle del Cauca/vas_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca_ERA.nc'
data = xr.open_dataset(r)

''' Establecemos las dimensiones espaciales para las coordenadas del archivo netCDF'''
data.rio.set_spatial_dims(x_dim='lon', y_dim='lat', inplace=True) #Ajustar etiquetas de lon longitude, lat latitude
data.rio.write_crs('EPSG:4326', inplace=True)

''' Importamos el SHP'''
shp = gpd.read_file('Datos/Poligono/Poligono.shp', crs='EPSG:4326')

'''Cortamos el archivo netCDF'''
corte = data.rio.clip(shp.geometry.apply(mapping), data.rio.crs, drop=True)

print(corte)
corte.to_netcdf('vas_3hr_GFDL-ESM4_ssp126_r1i1p1f1_gr1_201501010300-203501010000_ValleDelCauca_ERA_Mask.nc')

print('Corte realizado con exito')
#ax=shp.plot(facecolor='none',edgecolor='black')
#pak=corte.tas.isel(time=0).plot(ax=ax,zorder=-1) #Cambiar variable dependiendo del Archivo cargado
#plt.savefig('Dagua.png',dpi=300)
#plt.show()