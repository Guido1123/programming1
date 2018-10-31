try:
    mensen = int(input("Met hoeveel personen was u op reis? "))
    bedrag = 4356 / mensen
    if mensen <0:
        print("Negatieve getallen zijn niet toegestaan")
    else:
        print(bedrag)
except ValueError:
    print("Gebruik cijfers voor het invoeren van het aantal!")
except ZeroDivisionError:
    print("Delen door nul kan niet!")
except:
    print("Onjuiste invoer!")

