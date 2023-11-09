#==============================================================
#
#==============================================================
# from math import sqrt
# print(sqrt(10))
#==============================================================
#
#==============================================================
# import random

# print(random.randint(1, 100))

# fruits = ["apple","banana","orange"]
# print(random.choice(fruits))
#==============================================================
#
#==============================================================
# import time 
# print(time.time())
#==============================================================
#
#==============================================================
# import datetime
# now = datetime.datetime.now()
# print(now)
#==============================================================
#         Drukuje listę plików z obecnego folderu
#==============================================================
# import os
# for file in os.listdir():
#     print(file)
#==============================================================
#          Sprawdza czy plik z tą nazwą istnieje
#==============================================================
# file_path = "request.py"
# if os.path.exists(file_path):
#     print('file already exists')
#==============================================================
#   Program który sprawdza czy format daty jest prawidłowy
#==============================================================
import datetime
now = datetime.datetime.now()
print(now)

'dd-mm-yyyy'
todays_date = datetime . date.today()

print(todays_date)

print(datetime.date.fromtimestamp(10000000000).year)
a = datetime.datetime(2022,10,28,23,55,59,342380)
print(a)