lijst = ['a', 'b', 'c']
def wijzig(lijst):
    lijst.clear()
    lijst.append('d')
    lijst.append('e')
    lijst.append('f')
    return lijst

print(lijst)
wijzig(lijst)
print(lijst)