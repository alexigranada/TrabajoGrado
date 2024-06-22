import ee
#import geemap

# Inicializa Earth Engine
ee.Initialize()

# Define la región de interés (ROI) en forma de geometría (por ejemplo, un punto)
roi = ee.Geometry.Point(-75.55, 40.71)

# Define la colección de imágenes de GOES-16 ABI
goes16 = ee.ImageCollection('NOAA/GOES/16/MCMIPF')

# Filtra por la banda 13 y ajusta el rango de fechas (ejemplo)
image = goes16.filterDate('2023-01-01', '2023-01-02').select('CMI_C13')

# Obtén la primera imagen (puedes ajustar este paso según tus necesidades)
image = ee.Image(image.first())

# Visualiza la imagen (opcional)
#map = geemap.Map(center=[40.71, -75.55], zoom=8)
#map.addLayer(image, {'min': 0, 'max': 400}, 'GOES-16 Band 13')
#map.addLayer(roi, {'color': 'red'}, 'ROI')
#map.addLayerControl()
#map

# Descarga la imagen como una matriz de valores
data = image.sample(region=roi, scale=1000).getInfo()

# Accede a los valores de la banda 13
radiance = data['features'][0]['properties']['CMI_C13']

# Realiza la conversión a temperatura de superficie (ejemplo básico)
def rad2temp(radiance):
    # Constantes físicas
    c1 = 1.1910427e-5
    c2 = 1.4387752e2
    
    temp = c2 / (ee.Image(radiance).log().multiply(-1).add(c1)).toDouble().rename('temperature')
    return temp

# Calcula la temperatura de superficie
temperature = rad2temp(radiance)

# Imprime la temperatura (en Kelvin)
print('Temperatura de superficie (Kelvin):', temperature.getInfo())

# Obtén el valor numérico de la temperatura (en Kelvin)
temperature_value = temperature.reduceRegion(
    reducer=ee.Reducer.mean(),  # Puedes usar otros reductores según tu necesidad (mean, min, max, etc.)
    geometry=roi,
    scale=1000
).get('temperature').getInfo()

print('Temperatura de superficie (Kelvin):', temperature_value)