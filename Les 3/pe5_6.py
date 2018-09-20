klinker = ('aeiou')
text = input('geef een text:')
for xyz in text:
    if xyz in klinker:
        print(xyz)