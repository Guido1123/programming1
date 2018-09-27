def new_password(oldpassword, newpassword):
    cijfer1 = False
    for cijfers in newpassword:
        if cijfers in '0123456789':
            cijfer1 = True
    if newpassword != oldpassword and len(newpassword) >= 6 and cijfer1:
        return True
    else:
        return False

oldpassword = input('wat is je oude wachtwoord:')
newpassword = input('wat is je nieuwe wachtwoord:')
print(new_password(oldpassword,newpassword))


