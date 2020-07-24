value = int(input())

def check_prime(value):
    if value <= 1:
        return 'This number is not prime'
    else:
        for i in range(2,value):
            if value % i == 0 :
                return 'This number is not prime'
            else:
                continue
        return 'This number is prime'


result = check_prime(value)

print(result)