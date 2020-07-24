# put your python code here

number = int(input())

first_digit = int(number / 100)
second_digit = int((number % 100) / 10)
third_digit = number % 10

result = first_digit + second_digit + third_digit

print(result)