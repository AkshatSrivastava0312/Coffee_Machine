# put your python code here

a = int(input())
b = int(input())

keys = []

for value in range(a,b+1):
    if value % 3 == 0:
        x = value
        keys.append(x)

result = sum(keys)/len(keys)

print(result)
