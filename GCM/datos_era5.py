import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

''' 1. Cargar el conjunto de datos cdfNet (ejemplo: temperatura media diaria) '''
file = 'C:/Datos/ERA/adaptor.mars.internal-1710809115.0235066-15094-17-bfd0b32f-a82c-4b55-885f-2b4c217fc2c3.nc'
ds = xr.open_dataset(file)
print(ds)

temp = 't2m'  # Cambia 'temperatura' por la variable que estés interesado
latitud = 3.513  # Latitud del píxel de interés
longitud = -76.314  # Longitud del píxel de interés

# Crear una lista para almacenar los valores del píxel por fecha
temp_pixel = []

# Iterar sobre cada paso de tiempo
for tiempo in ds.time:
    # Extraer el valor del píxel en la ubicación y tiempo específicos
    valor_pixel = ds[temp].sel(latitude=latitud, longitude=longitud, method='nearest').sel(time=tiempo).values
    # Agregar el valor a la lista de valores del píxel por fecha
    temp_pixel.append(valor_pixel - 273.15)

# Mostrar los valores del píxel por fecha
for i, valor_pixel in enumerate(temp_pixel):
    print("Fecha:", ds.time[i].values, " - Valor del píxel:", valor_pixel)

''' Cargamos los datos de temperatura '''
#tas = ds['t2m']
#tas.data = tas.data - 273.15
#valor = tas.data
#time = tas['time']

#print(valor)
#print(tas)
#tas_mean = tas.mean('time', keep_attrs=True)
#tas_mean.data = tas_mean.data - 273.15
#valor = tas_mean.data
#print(tas_mean.data)
#Convertimos a °K a °C

#tas_mean.attrs['units'] = '°C'

''' Creamos Gráficas '''
''' Ploteamos precipitación nivel mundial '''
#fig = plt.figure(figsize=[12,5], dpi=200)
#ax = plt.subplot(1, 1, 1, projection=ccrs.PlateCarree())
#tas_mean.plot.pcolormesh(ax=ax,
                     #levels      = np.arange(0, 14, 1),
                     #extend      = 'max',
                     #transform   = ccrs.PlateCarree(),
                     #cbar_kwargs = {'label': tasmean.units},
                     #cmap = 'coolwarm' #'viridis_r'
                     #)
''' Add coast- and gridlines'''
#ax.coastlines(color='black')
#gl = ax.gridlines(draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
#gl.top_labels = False
#gl.right_labels = False
#gdf_valle.boundary.plot(ax=plt.gca(), color='black', linewidth=1, transform=ccrs.PlateCarree())
#gdf_dagua.boundary.plot(ax=plt.gca(), color='black', linewidth=1, transform=ccrs.PlateCarree())
#model = ds.attrs['Conventions']
#title = f'[{model}] Temperatura promedio'
#plt.title(title, fontsize=16, pad=20)
#plt.show()
