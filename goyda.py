import random
a = random.randint(1,100)
b = random.randint(1,100)
c = random.randint(1,100)
d = random.randint(1,100)
e = random.randint(1,100)
f = random.randint(1,100)
g = random.randint(1,100)
h = random.randint(1,100)
list = [a,b,c,d,e,f,g,h]
list.sort()
num = random.randint(1,8)
print (list)
answer = list[num]
print (answer)
ingame = True
print("This is a binary search game,try to guess using binary search")
while ingame == True:
    guess = int(input("Try to guess the random number \n"))
    if guess < answer:
        print("Wrong, your guess is smaller")
    elif guess > answer:
        print("Wrong, your guess is bigger")
    elif guess == answer:
        print("YOU GUESSED IT")
        ingame = False    