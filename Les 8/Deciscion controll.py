def seizoen(maand):
    if maand >= 12:
        seizoen= "het is winter"
    elif maand >= 9:
        seizoen= "Het is herfst"
    elif maand >= 6:
        seizoen = "het is zomer"
    elif maand >= 3:
        seizoen = "Het is lente"
    else:
        seizoen = "Het is winter"
    return seizoen
maand=int(input("voer hier het maand nummer in: "))
print(seizoen(maand))

