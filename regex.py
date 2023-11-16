# findall - zwraca listę zawierającą wszystkie wystąpienia 
# search - zwraca obiekt match, jeśli w dowolnym miejscu znajdzie dopasowanie
# split - zwraca listę, w której ciągu znaków został podzielony przy każdym dopasowaniu
# sub - zastępuje jedno lub więcej wystąpień

#[a-z] - zwraca dopasowania pasujące do wzoru od a-z, male litery
#[a-k]
#[0-9] - 
#[678]
#[^michal] -> "c" ale "ch" nie
# dla 00-62
#[0-6][0-9] -> "56" ale "72" nie
#[+] - dowolny znak -> @
import re


txt = "Dopasowuje pozycję, która nie jest granicą słowa."
x = re.search("^Dopasowuje.*słowa.$", txt)
print(x)



txt = "Dopasowuje nie pozycję, nie która nie jest ngranicą nie słowa."

# x = re.findall("nie", txt)
# print(x)

# x=re.split("\s",txt)
# print(x)

# x=re.sub("nie","WOW",txt,1)
# print(x)

# x = re.findall(r"[\w\.]+",txt)
# print(x)

# mail = "lubie.placki@pw.eud.pl"

# x=re.split("@",mail)
# print(x)

# x=re.match("^[\w\.]+@[\w\.]+",mail)
# print(x)

# txt1= "Rok 2023 bedzie lepszy"

# x=re.sub("\d",'X',txt1)
# print(x)

# x=re.findall(r"\b[n]\w+",txt)
# print(x)

# kot = "Nasz kot ma 60 lat i waży 4kg"
# x = re.findall(r"\d+",kot)
# print(x)

# x = re.search(r"^nasz",kot,re.IGNORECASE)
# print(x)

# tel = "Moj numer to 123-456-7890"
# x= re.search(r"\d{3}-\d{3}-\d{4}",tel)
# print(x)

text = "Odiwdzź https://www.exmple.com i http://www.anotherdomain.org"
domain_names = re.findall(r"https?://www\.(\w+)", text)
print(domain_names)