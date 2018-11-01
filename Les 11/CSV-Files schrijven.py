import datetime
import csv

bestand = 'inloggers.csv'
while True:
    naam = input("Wat is je naam? ")
    if naam == 'einde':
        break
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")
    with open('inloggers.csv', 'w', newline='')as inloggers:
        vandaag = datetime.datetime.today()
        Tijd = vandaag.strftime("%a %d %b %Y %H:%M:%S ")
        output = csv.writer(inloggers, delimiter=',')
        output.writerow([Tijd, naam, voorl, gbdatum, email])
