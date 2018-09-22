def standaardprijs(afstandKM):
    if afstandKM>50:
       getal=15+afstandKM*0.60
    else:
        if afstandKM<0:
            afstandKM == 0
        getal=afstandKM*0.80
    return getal

def ritprijs(leeftijd, weekendrit, afstandKM):
    if weekendrit == ('zaterdag') or weekendrit == ('zondag'):
        print('true')
        if leeftijd > 64 or leeftijd < 12:
            print(standaardprijs(afstandKM)-(standaardprijs(afstandKM)/100*35))
        else:
                print(standaardprijs(afstandKM)-(standaardprijs(afstandKM)/100*40))
    else:
        print("False")
        if leeftijd < 12 or leeftijd >= 65:
            print(standaardprijs(afstandKM)-(standaardprijs(afstandKM)/100*30))
        else:
            print(standaardprijs(afstandKM))
    return
afstandKM = eval(input('hoeveel kilometer gaat u reizen?: '))
print(standaardprijs(afstandKM))
weekendrit =(input('op welke dag gaat u reizen?: '))
leeftijd = eval(input('hoe oud bent u?: '))
ritprijs(leeftijd, weekendrit, afstandKM)


