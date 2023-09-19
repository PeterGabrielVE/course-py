from datetime import datetime, timedelta

fecha1 = datetime(2023, 1, 1) + timedelta(weeks=1)
fecha2 = datetime(2023, 2, 1)

delta = fecha2 - fecha1
print(delta)
print("days", delta.days)
print("seconds", delta.seconds)
print("microseconds", delta.microseconds)