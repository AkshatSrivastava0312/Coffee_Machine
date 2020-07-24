value=int(input())
flag=0
while value<700000:
    value=value+(value*0.071)
    flag+=1

print(flag)