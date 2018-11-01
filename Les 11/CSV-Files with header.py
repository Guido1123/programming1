import csv

with open('CSVheader.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    duurste=0
    duursteproduct=[]
    aantal=600
    minste=[]
    voorraad=0
    for row in csv_reader:
        if line_count == 0: #dit is de 1e regel, kunnen we niks mee
            line_count += 1 #zorgt ervoor dat je hier niet meer terugkomt.
        else:
            voorraad += int(row[3])
            if float(row[4]) > float(duurste):
                duurste = row[4]
                duursteproduct = row
            if float(row[3])<float(aantal):
                aantal=row[3]
                minste=row
        #print(f'Artikelnummer: {row[0]}, Code: {row[1]}, Naam: {row[2]}, Voorraad: {row[3]}, Prijs:{row[4]}.')
print('Het duurste artikel is {} en die kost {} Euro'.format(duursteproduct[2],duursteproduct[4]))
print('Het duurste artikel is '+(duursteproduct[2])+' en die kost '+ str(duursteproduct[4])+ ' Euro')
print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(minste[3],minste[0]))
print('In totaal hebben wij {} producten in ons magazijn liggen'.format(voorraad))
print('In totaal hebben wij ' +str(voorraad)+' producten in ons magazijn liggen')