# put your python code here

year = int (input())

def check_leap(year) :
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
        return 'Leap'
    else:
        return 'Ordinary'

ans = check_leap(year)

print(ans)