from random import randint
life = 0
x = randint(1,10)
reslife = 4 - life
print("you have 3 lifes so be carefull :)")
while life<3:
    reslife -= 1
    print("you have only "+str(reslife)+ " lifes")
    num= input("awnser is a number between 1 to 10: ")
    num = int(num)
    if x<num:
        print("your awnser is bigger than that number ")
        life +=1
    elif x>num:
        print("your awnser is smaller than that number")
        life +=1
    else:
        print("welldone! your awnser is correct")
        input("Press enter to exit!")
        quit()
x = str(x)
print("game over :( that number was "+ x)