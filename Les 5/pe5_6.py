klinker = ('aeiou')
text = input('geef een text:')
for char in text:
    if char in klinker:
        print(char)