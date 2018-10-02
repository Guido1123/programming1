list=(input("Geef lijst met minimaal 10 strings: "))
outfile = open("strings.txt", "w")
outfile.write(list)
outfile.close()
infile=open("strings.txt",'r')
regel=infile.readlines()
letters=''
for words in regel:
    woord=words.split("\", \"")
    #print(woord)
    outfile = open("strings.txt", 'a')
    outfile.write('\nDe nieuwgemaakte lijst is: ')
    for letter in woord:
        if len(letter) == 4:
            letters+=letter
            outfile.write('\''+letter+'\', ')

outfile.close()