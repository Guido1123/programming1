def berekeningsom (getallenlijst):
    som = 0
    for getal in getallenlijst:
        som = som + getal
    return som

getallenlijst = [1,2,3]
print(berekeningsom(getallenlijst))