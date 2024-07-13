# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 18:52:43 2024
Aplicando remuestreo bicubico a los datos DEM AlosPalsar para escalarlos a 0.1°
@author: Arturo A. Granada G.
"""

import xarray as xr
import rioxarray
#import scipy.ndimage
from scipy.ndimage import zoom
import numpy as np

''' Cargar el archivo DEM y el Raster '''
dem_original = rioxarray.open_rasterio('Datos/DEM_Mask.tif')
dem_destino = rioxarray.open_rasterio('Datos/ERA_PARA_DEM.tif')


if 'band' in dem_original.dims:
    dem_original = dem_original.isel(band=0)

# Suponiendo que la resolución actual es de 30 metros por píxel
escala_x = dem_original.rio.resolution()[0] / dem_destino.rio.resolution()[0]
escala_y = dem_original.rio.resolution()[1] / dem_destino.rio.resolution()[1]

# Remuestrear los datos
# Asegúrate de que las escalas sean correctas; puedes necesitar ajustar +/- signos dependiendo de la dirección de los ejes
data_resampled = zoom(dem_original.values, (escala_y, escala_x), order=3)  # Usamos interpolación bilineal

# Crear un nuevo DataArray
dem_resampled = xr.DataArray(
    data_resampled,
    dims=["y", "x"],
    coords={
        "y": np.linspace(dem_destino.y[0], dem_destino.y[-1], data_resampled.shape[0]),
        "x": np.linspace(dem_destino.x[0], dem_destino.x[-1], data_resampled.shape[1])
    }
)

# Añadir los metadatos necesarios para guardar como raster
dem_resampled.rio.write_crs(dem_original.rio.crs, inplace=True)
dem_resampled.rio.write_transform(dem_destino.rio.transform(), inplace=True)

# Guardar el DEM remuestreado
dem_resampled.rio.to_raster('DEM_RE_ERA_3.tif')

print('Proceso finalizado.')