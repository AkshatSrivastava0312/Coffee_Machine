number = int(input())
word = input()

# write a condition for plurals
if number!=1:
    word=word.__add__('s')


print(number, word)