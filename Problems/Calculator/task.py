# put your python code here

first_number=float(input())
second_number=float(input())
operator=str(input())

if second_number==0 and operator in ['/','mod','div']:
    print('Division by 0!')
elif operator=='+':
    print(first_number+second_number)
elif operator=='-':
    print(first_number-second_number)
elif operator=='/':
    print(first_number/second_number)
elif operator=='*':
    print(first_number*second_number)
elif operator=='mod':
    print(first_number%second_number)
elif operator=='pow':
    print(first_number**second_number)
elif operator=='div':
    print(first_number//second_number)


