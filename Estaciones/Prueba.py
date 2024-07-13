'''Importamos librerias'''
from datetime import datetime, timedelta

start_date = datetime(2024, 3, 29, 0, 0)  # Fecha de inicio
end_date = datetime(2024, 3, 29, 23, 59)  # Fecha de fin

current_date = start_date
while current_date <= end_date:
    print(current_date)
    current_date += timedelta(minutes=1)
    print(current_date.strftime('%Y-%m-%d %H:%M'))