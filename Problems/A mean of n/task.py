n = int(input())

values = []

for val in range(n):
    val = int(input())
    values.append(val)


result = float(sum(values)/len(values))

print(result)