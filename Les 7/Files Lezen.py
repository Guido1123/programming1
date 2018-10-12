infile=open ('klantenkaartnummer.txt')
regels= infile.readlines()
infile.close()
print(regels)

for regel in regels:
    kaartinfo = regel.split(',')
    #print(kaartinfo[1].strip() + ' heeft kaartnummer: '+ kaartinfo[0])
    print("{} heeft kaartnummer: {}".format(kaartinfo[1].strip(),kaartinfo[0]))