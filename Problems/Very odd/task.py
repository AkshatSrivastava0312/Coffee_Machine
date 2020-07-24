dividend = int(input())
divisor = int(input())

def check_if_odd(a,b) :
    if (a / b) % 2 == 1 :
        return True
    else :
        return False

result = check_if_odd(dividend,divisor)

print(result)