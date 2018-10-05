infile= open("Kluizen.txt", "r")
regels=infile.readlines()
print("1: Ik wil weten hoeveel kluizen nog vrij zijn\n2: Ik wil een nieuwe kluis\n3: Ik wil even iets uit mijn kluis halen\n4: Ik geef mijn kluis terug")
menukeuze = int(input("Maak uw keuze:"))
def toon_aantal_kluizen_vrij():
    regel=0
    for i in regels:
        regel+=1
    print(12-regel)
def nieuwe_kluis():
    kluisnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for gedeelte in regels:
        splitsels= gedeelte.split(";")
        if int(splitsels[0]) in kluisnummers:
            kluisnummers.pop(kluisnummers.index(int(splitsels[0])))
    if len(kluisnummers) == 0:
        print("Er zijn helaas geen kluizen meer beschikbaar!")
    else:
        print(kluisnummers)
        infile.close()
        password= input("Geef een wachtwoord van minimaal 4 characters:")
        if len(password) >= 4:
            outfile= open("Kluizen.txt","a" )
            outfile.write(str(kluisnummers[0])+";"+ password+"\n")
            outfile.close()
            print("Jouw is kluisnummer "+str(kluisnummers[0])+" Toegewezen")
        else:
            print("Zorg ervoor dat het wachtwoord minimaal 4 characters bevat")
def kluis_openen():
    nummer= input("wat is je kluisnummer kneus?:")
    code= input("Weet je überhaupt je code nog ? zo ja vul hem dan hier in :")
    for gedeelte in regels:
        splitsels=gedeelte.split(";")
        splitsels[0],splitsels[1].strip()
        if nummer in splitsels[0] and code in splitsels[1]:
            print("Uw kluis is geopend ")
    if nummer not in splitsels[0] or code not in splitsels[1]:
         print("Verkeerd wachtwoord of kluisnummer ")

if menukeuze == 1:
    toon_aantal_kluizen_vrij()
elif menukeuze == 2:
    nieuwe_kluis()
elif menukeuze == 3:
    kluis_openen()
elif menukeuze == 4:
    pass
else:
    print("Geef astublieft een geldige waarde!")