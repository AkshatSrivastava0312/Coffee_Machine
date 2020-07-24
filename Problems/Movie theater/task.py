halls = int(input())
capacity = int(input())
viewers = int(input())

def check_possibility(halls,capacity,viewers) :
    if viewers <= halls * capacity :
        return True
    else :
        return False

print(check_possibility(halls,capacity,viewers))