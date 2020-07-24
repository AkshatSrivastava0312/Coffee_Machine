money=int(input())

chicken=23
goat=678
pig=1296
cow=3848
sheep=6769

if money<chicken:
    print('None')
elif chicken <= money < goat:
    print(money//chicken , 'chicken' if money//chicken==1 else 'chickens')
elif goat<=money<pig:
    print(money//goat,'goat' if money//goat==1 else 'goats')
elif pig<=money<cow:
    print(money//pig,'pig' if money//pig==1 else 'pigs')
elif cow<=money<sheep:
    print(money//cow,'cow' if money//cow==1 else 'cows')
else:
    print(money//sheep,'sheep')