import json

PATH = "pole.json"

def calculate_field_area(lengh : float, width : float): # Liczy pwierzchnię z podanych danych
    return lengh*width

def load(): # Wczytuje dane z pliku
    try:
        with open(PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

DATA = load()

def save(): # Zapisuje dane do pliku
    with open(PATH, 'w') as f:
        json.dump(DATA, f, indent = 4)
    print("Saved")

def scherch_rolnik_info(nazwa_rolnika, x = 0): # Wyszukuje rolnika gdy x jest różny od 0 a gdy x równy 0 to wyświetla danego rolnika
    for id,rolnik in DATA.items():
        if rolnik["nazwa_rolnika"] == nazwa_rolnika:
            if x != 0:
                return id
            elif x == 0:
                print(f"Rolnik: {rolnik["nazwa_rolnika"]}, liczba działek: {rolnik["liczba_działek"]}, łączna powierzchnia: {rolnik["łączna_powierchnia"]}, oraz wszystkie działki: {rolnik["diałki"]}")
                return
    return False
    
def add_rolnik(nazwa_rolnika): # Dodaje rolnika !!!ROLNIK MUSI MIEĆ UNIKALNĄ NAZWĘ!!! (program odrzuci próbę dodania drugiego rolnika z tą samą nazwą)
    if not scherch_rolnik_info(nazwa_rolnika, 1):
        id = len(DATA) + 1
        DATA[id] = {'nazwa_rolnika':nazwa_rolnika,
                    'liczba_działek': 0,
                    'diałki': {},
                    'łączna_powierchnia': 0}
        print("Rolnik added")
        save()
    else:
        print("Taki rolnik już istnieje")

def calculate_total_area(nazwa_rolnika): # Oblicza łączną powierzchnię wszystkich działek rolnika
    if scherch_rolnik_info(nazwa_rolnika, 1):
        id = scherch_rolnik_info(nazwa_rolnika, 1)
        count = int(DATA[id]["liczba_działek"])
        suma = 0
        while count != 0:
            lengh, width = DATA[id]["diałki"][str(count)].split("X")
            suma = suma + calculate_field_area(float(lengh), float(width))
            count = count-1
        DATA[id]["łączna_powierchnia"] = suma
        save()
    else:
        print("Nie ma takiego rolnika w systemie")
        return False

def add_field(nazwa_rolnika, lengh : float, width : float): # Dodaje działkę o wymiarach lengh i width do rolnika
    if scherch_rolnik_info(nazwa_rolnika, 1):
        id = scherch_rolnik_info(nazwa_rolnika, 1)
        liczba_działek = int(DATA[id]["liczba_działek"]) + 1
        DATA[id]["liczba_działek"] = liczba_działek
        DATA[id]["diałki"][str(liczba_działek)] = f"{lengh}X{width}"
        calculate_total_area(nazwa_rolnika)
        print("Field added")
    else:
        print("Nie ma takiego rolnika w systemie, musisz go najpierw dodać funkcją [add_rolnik]")
        return False

def show_all(): # Wyświetla wszystkich rolników i ich działki
    for id,rolnik in DATA.items():
        print(f"Rolnik: {rolnik["nazwa_rolnika"]}, liczba działek: {rolnik["liczba_działek"]}, łączna powierzchnia: {rolnik["łączna_powierchnia"]}, oraz wszystkie działki: {rolnik["diałki"]}")
