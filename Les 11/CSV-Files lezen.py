import csv

with open('gamerinfo.csv', mode='r') as csv_file:
    scoreboard = csv.reader(csv_file, delimiter=';')
    winning=0
    winnaar=[]
    for row in scoreboard:
        if int(row[2])>int(winning):
            winning=row[2]
            winnaar=row
    print("De hoogste score is: {} op {} behaald door {}".format(winnaar[2], winnaar[1], winnaar[0]))
