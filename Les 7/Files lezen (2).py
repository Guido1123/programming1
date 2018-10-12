infile= open('Klantenkaartnummer.txt','r')
regels = infile.readlines()
count=0
hoogste=0
for regel in regels:
    kaartinfo = regel.split(', ')
    count = count + 1
    if int(kaartinfo[0])> int(hoogste):
        hoogste=kaartinfo[0]


print('Deze file telt {} regels. \nHet grootste kaartnummer is: {} en dat staat op regel {}.'.format(count,hoogste,int(max(regel[0]))+1))