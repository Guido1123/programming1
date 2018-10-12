import datetime
outfile = open("hardloper.txt" , "a")
name = input("wat is je naam?: ")
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y %H:%M:%S "+ name + "\n" )
outfile.write(s)
outfile.close()