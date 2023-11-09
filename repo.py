import requests
#waluta_z
#waluta_na
#kwote
def przelicz(kwote:float, walute_z:str, walute_na:str,) -> float:
    url = "https://v6.exchangerate-api.com/v6/f34f2fba43f04e7b511315d0/latest/{walute_z}"
    response = requests.get(url)
    lista_walut = response.json()['conversation_rates']
    wynik = kwota * lista_walut[waluta_na]
    return wynik
print(przelicz(100, "USD", "PLN"))