def gemiddelde(zin):
    outfile = open("zin.txt", "w")
    outfile.write(zin)
    outfile.close()
    infile=open("zin.txt",'r')
    regel=infile.readlines()
    letters=0
    for words in regel:
        woord=words.split(" ")
        for letter in woord:
            letters+=len(letter)
        print(letters/len(woord))
zin=input("Zeg een zin: ")
gemiddelde(zin)
