def new_password(oldpassword, newpassword):
    for cijfers in newpassword:
        if cijfers in '0123456789':
            cijfers = True
        else:
            cijfers = False
    if oldpassword != newpassword and len(newpassword)>= 6 and cijfers:
        return 'je wachtwoord is geweizigd'
    else:
        return 'je wachtwoord is niet geweizigt'





oldpassword = input('wat is je oude wachtwoord:')
newpassword = input('wat is je nieuwe wachtwoord:')
print(new_password(oldpassword, newpassword))