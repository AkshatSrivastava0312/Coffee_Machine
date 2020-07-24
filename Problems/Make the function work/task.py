def closest_higher_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        while (x % 5 != 0):
            x=x+1
        return x
