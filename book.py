
#===============================
#[X] list()
#[X] add(tytuł, autor, rok)
#[X] save()
#[X] delete(id)
#[X] edit(id, tytuł, autor, rok)
#[ ] search(kryterium,wartość)
#===============================

import json

path_book = 'database_book.json'

def load(path):
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {} 

def save(path, database):
    with open(path,'w') as file:
        json.dump(database, file, indent=4)

def add(database, tytul, autor, rok):
    # if id in database:
    #     raise ValueError("Książka o takim ID Już istnieje.")
    id = len(database) + 1

    database[id] = {'tytul':tytul,
                    'autor':autor,
                    'rok':rok}

def delete(database, id):
    if id not in database:
        raise ValueError("Nie znaleziono ksiązki o tym ID")
    del database[id]

def edit(database, id, tytul=None, autor=None, rok=None):
    if id not in database:
        raise ValueError("Nie znaleziono ksiązki o tym ID")
    if tytul:
        database[id]['tytul'] = tytul
    if autor:
        database[id]['autor'] = autor
    if rok:
        database[id]['rok'] = rok

def search(database, kryterium, argument):
    if kryterium == "tytul":
        for id, book in database.items():
            if book['tytul'] == argument:
                print(f"ID:{id} , tytul: {book['tytul']}, Autor: {book['autor']}, Rok: {book['rok']}")
    elif kryterium == "autor":
        for id, book in database.items():
            if book['autor'] == argument:
                print(f"ID:{id} , tytul: {book['tytul']}, Autor: {book['autor']}, Rok: {book['rok']}")
    elif kryterium == "rok":
        for id, book in database.items():
            if book['rok'] == argument:
                print(f"ID:{id} , tytul: {book['tytul']}, Autor: {book['autor']}, Rok: {book['rok']}")
    else:
        raise ValueError("Nie ma takiego kryterium")

def book_list(database):
    for id, book in database.items():
        print(f"ID:{id} , tytul: {book['tytul']}, Autor: {book['autor']}, Rok: {book['rok']}")



database = load(path_book)

#add(database, 'Python dla bystrzaków','Nolan Illes',2012)
#book_list(database)


search(database, "autor", "Nolan Illes")











save(path_book, database)