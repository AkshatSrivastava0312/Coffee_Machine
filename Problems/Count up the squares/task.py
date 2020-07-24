# put your python code here

result = 0
list = 0
while True:
    value = int(input())
    list += value
    result += value ** 2
    if list == 0:
        break

print(result)