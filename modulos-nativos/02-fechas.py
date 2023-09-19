#import time

#print(time.time())

from datetime import datetime

fecha = datetime(2023, 1, 1)
#print(fecha)

now = datetime.now()
#print(now)

fechaStr = datetime.strptime("2023-01-01","%Y-%m-%d")
print(fechaStr)