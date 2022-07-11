import random
computer=random.randint(1,100)
player=0
tries=0
print("guss the number game")
while(player!=computer):
    player=int(input("enter the number :"))
    tries=tries+1
    if(player<computer):
        print("too low,try again")
    elif(player>computer):
        print("too high,try again")
    else:
        print("correct!,you got it",tries,"tries")