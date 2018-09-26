def convert(Celsius):
    Fahrenheit = Celsius*1.8+32
    return Fahrenheit


def tabel(temp):
    for c in temp:
        convert(c)
        print("{:5}  {:5}".format((convert(c)),c))
    return


temp = range(-30,41,10)
tabel(temp)
