from datetime import datetime
from datetime import timedelta
import locale
locale.setlocale(locale.LC_ALL, 'pl_PL')
now = datetime.now()
print(now)

print(now.year)

print(now.strftime("%B"))

print(now + timedelta(days=5))

print(now + timedelta(weeks=2))

urodziny = datetime(1990, 5, 28)
roznica = now - urodziny
lat = roznica.days / 365
print(lat.__round__(None))