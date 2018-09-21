def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and len(newpassword) >= 6:
        print('true')
    else:
        print('false')
    return new_password

oldpassword = input('wat is je oude wachtwoord:')
newpassword = input('wat is je nieuwe wachtwoord:')

new_password(oldpassword, newpassword)