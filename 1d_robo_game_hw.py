from os import system
#DATA#
roboX  = 5
bombX  = 17
bombX2 = 3
roboHP = 100
coins  = 11
LENGHT = 20
roboBT = 100
score = 0 
hearts = 14

print()
#MAP#
while True:
    system('cls')
    
    for x in range(1, LENGHT+1):
       
        if x == roboX:
            print("🤖", end="")
        elif x==bombX:
            print("💣", end="")
        elif x==bombX2:
            print("💣", end="")
        elif x==hearts:
            print("💙", end="")
        elif x == coins:
            print("💰", end="")
        else:
            print(".", end="")
    print("\nHP: ",roboHP)
    print("BT: ",roboBT)
    print("Coins: ",score)
    print("\n")
#DECIDE#   
    option = input(">>> " )
    if option == 'a' and roboX >1:
        roboX -=1
        roboBT -=1
    if option =='d' and roboX< LENGHT:
        roboX +=1
        roboBT -=1
    if option =='x':
        break
    if bombX == roboX:
        roboHP -=10
    if bombX2 == roboX:
        roboHP -=10
    if roboHP ==0:
        print("You are dead!")
        break
    if roboX == coins:
        score += 10
    if roboX == hearts and roboHP<100:
        roboHP += 10
    if roboBT ==0:
        print("You are out of batery")
        break
print("Try again!")