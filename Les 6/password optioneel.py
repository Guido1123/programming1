def new_password(oldpassword, newpassword):
    cijfer1 = 0
    for cijfers in newpassword:
        if cijfers in '0123456789':
            cijfer1 = 1
    if newpassword != oldpassword and len(newpassword) >= 6 and cijfer1 == 1:
        print('true')
    else:
        print('false')

oldpassword = input('wat is je oude wachtwoord:')
newpassword = input('wat is je nieuwe wachtwoord:')
new_password(oldpassword,newpassword)


