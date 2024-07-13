# -*- coding: utf-8 -*-
"""
Created on Thu May 09 07:54:01 2024

Descarga de datos ERA5 Land Hours (Temperatura cerca a la superficie de la tierra)

@author: Arturo A. Granada G.
"""
import xarray as xr
import requests
import netCDF4
import boto3
import os
from botocore.config import Config
from botocore import UNSIGNED
import datetime

# Configuración inicial
bucket_name = 'noaa-goes16'
year = 2018

# Productos y bandas
products = {
    'ABI-L2-RRQPEF': None,
    'ABI-L2-LSTF': None
}

# Carpeta raíz de descarga
root_download_folder = "D:/Goes"
os.makedirs(root_download_folder, exist_ok=True)

# Crear carpetas para cada producto
for product in products.keys():
    product_folder = os.path.join(root_download_folder, product)
    os.makedirs(product_folder, exist_ok=True)

# Inicializar el cliente S3 sin firma
s3_client = boto3.client('s3', config=Config(signature_version=UNSIGNED))

# Función para obtener las claves S3
def get_s3_keys(bucket, s3_client, prefix=''):
    kwargs = {'Bucket': bucket, 'Prefix': prefix}
    while True:
        resp = s3_client.list_objects_v2(**kwargs)
        for obj in resp.get('Contents', []):
            yield obj['Key']
        if not resp.get('IsTruncated'):  # Salir del bucle si no hay más datos
            break
        kwargs['ContinuationToken'] = resp['NextContinuationToken']

# Función para descargar y guardar los datos
def download_and_save_data(date, hour, product, band=None):
    product_folder = os.path.join(root_download_folder, product)
    if band is not None:
        prefix = f'{product}/{year}/{date.timetuple().tm_yday:03d}/{hour:02d}/OR_{product}-M3C{band:02d}'
    else:
        prefix = f'{product}/{year}/{date.timetuple().tm_yday:03d}/{hour:02d}/OR_{product}'

    keys = list(get_s3_keys(bucket_name, s3_client, prefix))
    if keys:
        key = keys[0]  # Tomar la primera clave
        resp = requests.get(f'https://{bucket_name}.s3.amazonaws.com/{key}')
        file_name = key.split('/')[-1].split('.')[0]
        nc4_ds = netCDF4.Dataset(file_name, memory=resp.content)
        store = xr.backends.NetCDF4DataStore(nc4_ds)
        DS = xr.open_dataset(store)
        DS.to_netcdf(os.path.join(product_folder, f'{file_name}.nc'))  # Guardar en la carpeta del producto

# Iterar a través de las fechas y horas
start_date = datetime.datetime(year, 1, 1)
end_date = datetime.datetime(year, 12, 31)  
current_date = start_date

while current_date <= end_date:
    for hour in range(24):
        for product, bands in products.items():
            if bands:
                for band in bands:
                    download_and_save_data(current_date, hour, product, band)
            else:
                download_and_save_data(current_date, hour, product)
    current_date += datetime.timedelta(days=1)










