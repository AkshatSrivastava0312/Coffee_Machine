jack_age = int(input())
alex_age = int(input())
lana_age = int(input())

if jack_age < alex_age and jack_age < lana_age :
    print(jack_age)
elif alex_age < jack_age and alex_age < lana_age :
    print(alex_age)
elif lana_age < jack_age and lana_age < alex_age :
    print(lana_age)

