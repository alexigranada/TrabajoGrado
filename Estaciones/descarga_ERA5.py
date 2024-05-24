# -*- coding: utf-8 -*-
"""
Created on Wed Mar  18 10:49:55 2024
Descarga datos ERA5 por medio de la API
@author: Arturo A. Granada G.
"""

import cdsapi

def descargar_datos_era5(years, months, output_dir):
    c = cdsapi.Client()

    for year in years:
        for month in months:
            c.retrieve(
                'reanalysis-era5-land',
                {
                    'year': str(year),
                    'variable': [
                        '10m_u_component_of_wind',
                        '10m_v_component_of_wind',
                        #'2m_dewpoint_temperature',
                        '2m_temperature',
                        #'evaporation_from_vegetation_transpiration',
                        #'leaf_area_index_high_vegetation',
                        #'leaf_area_index_low_vegetation',
                        #'surface_net_solar_radiation',
                        'surface_pressure',
                        'total_evaporation',
                        'total_precipitation',
                        #'total_precipitation_hourly',
                    ],
                    'month': str(month).zfill(2),
                    'time': [
                        '00:00', '01:00', '02:00',
                        '03:00', '04:00', '05:00',
                        '06:00', '07:00', '08:00',
                        '09:00', '10:00', '11:00',
                        '12:00', '13:00', '14:00',
                        '15:00', '16:00', '17:00',
                        '18:00', '19:00', '20:00',
                        '21:00', '22:00', '23:00',
                    ],
                    'day': [
                        '01', '02', '03',
                        '04', '05', '06',
                        '07', '08', '09',
                        '10', '11', '12',
                        '13', '14', '15',
                        '16', '17', '18',
                        '19', '20', '21',
                        '22', '23', '24',
                        '25', '26', '27',
                        '28', '29', '30',
                        '31',
                    ],
                    'format': 'netcdf',
                    'area': [
                        4, -77.5, 3.3,
                        -76.2,
                    ],
                },
                f"{output_dir}/era5_{str(month).zfill(2)}{str(year)}.nc"
            )
descargar_datos_era5(range(2017, 2023), range(1, 13), "D:/Usuario/Documents/ERA5_VC_9KM")
print('¡Completado!')