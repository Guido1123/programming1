def lang_genoeg(lengte):
    if lengte >= 120:
        print("je bent lang genoeg voor de attractie!")
    if lengte <= 120:
        print("sorry je bent te klein")
    return lengte

lengte = int(input('wat is je lengte:'))
lang_genoeg(lengte)

