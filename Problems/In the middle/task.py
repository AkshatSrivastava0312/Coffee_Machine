# don't modify this code
# a stores an input value
a = int(input().strip())

# put your code here

def check_input (val) :
    if val < 10 or val > 250 :
        return True
    else :
        return False

print(check_input(a))