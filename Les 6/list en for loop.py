grondgetallen = [4, 5, 3, -81]
def kwadraten_som(grondgetallen):
    som = 0
    for i in grondgetallen:
        if i > 0:
           som += (i**2)
    return som

print(kwadraten_som(grondgetallen))