def lang_genoeg(lengte):
    if lengte >= 120:
        print("je mag de attractie in!")
    if lengte <= 120:
        print("je bent te klein sorry!")
    return lengte

lengte = int(input('wat is je lengte:'))
(lang_genoeg(lengte))

