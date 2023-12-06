import requests
# response = requests.get('https://www.google.com/')
# print(response.text)

#czy jest @
#jaki jest username
#zakres  6-30 znaków
#jaka jest domena
#czy składa się z znaków dozwolonych
#email = input("Podaj swój adres e-mail: ")
def validate_email(email):
    if email.count('@') != 1:
        raise ValueError("To nie jest adres mailowy!")
        
    param = email.split('@')
    print(param)

try:
    validate_email('boguckipw.edu.pl')
except ValueError as e:
    print(f"Kod błędu: {e}")