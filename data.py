#==============================================================
#           Pobiera z bioblioteki funkcie
#==============================================================
from datetime import datetime
from datetime import date
from datetime import timedelta
#==============================================================
#                  Wyświetla obecną datę
#==============================================================
now = datetime.now()
print(now)
print(now.year)
print(now.strftime("%Y"))
#==============================================================
#           Wyświetla nazwę aktualnego mieśąca
#==============================================================
print(now.strftime("%B"))
#==============================================================
#         Wyświetla nazwę aktualnego dnia tygodnia
#==============================================================
print(now.strftime("%A"))
#==============================================================
#          konwerter zapisanej daty na obiekt daty
#==============================================================
date_object = datetime.strptime("2023-11-15", "%Y-%m-%d")
print(date_object)
#==============================================================
#                Dodaje to pewnej daty 5 dni
#==============================================================
date_object = datetime.strptime("2023-11-15", "%Y-%m-%d")
new_date = date_object + timedelta(days=5)
print(new_date)
#==============================================================
#          konwerter zapisanej daty na obiekt daty
#==============================================================
print(now-timedelta(weeks=2))
#==============================================================
#          sprawdza ile dni upłyneło od danej daty
#==============================================================
date_first = datetime(2023, 1, 1)
day = now - date_first
print(day.days)
#==============================================================
#          Sprawdza czy rok jest przestępny
#==============================================================
import calendar
new_year = calendar.isleap(2024)
if new_year:
    print("Ten rok jest przestępny")
else:
    print("Ten rok nie jest przestępny")
#==============================================================
#        Sprawdza który jest obecnie tydzień roku
#==============================================================
print(now.strftime("%U"))
#==============================================================
#                    Zmienia format daty
#==============================================================
rfc_date = datetime.strptime("2023-11-15 00:00:00", "%Y-%m-%d %H:%M:%S").strftime("%a,%d %b %Y %H:%M:%S +0000")
print(rfc_date)

date2 = datetime(now.year, 7, 4)
print(date2.strftime("%A"))