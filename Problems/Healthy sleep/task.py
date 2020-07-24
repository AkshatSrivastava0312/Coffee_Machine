a=int(input())
b=int(input())
h=int(input())

def check_sleep(a,b,h):
    if h<a:
        print('Deficiency')
    elif h>b:
        print('Excess')
    else:
        print('Normal')


check_sleep(a,b,h)