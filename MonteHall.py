# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:37:11 2024

@author: santo
"""

import random
doors=[0]*3
goatdoors=[0]*2
swap=0
dont_swap=0
j=0
win=0
while(j<5):
    x=random.randint(0,2)
    doors[x]="BMW"
    for i in range(0,3):
        if(i==x):
            continue
        else:
            doors[i]="Goat"
            goatdoors.append(i)
    choice=int(input("Enter your choice (0, 1, 2): "))
    door_open=random.choice(goatdoors)
    while(door_open==choice):
        door_open=random.choice(goatdoors)
    print(door_open)
    ch=input("Do you want to swap? y/n: ")
    if(ch=='y'):
        if(doors[choice]=='Goat'):
            print("player wins")
            #swap=swap+1
            win=win+1
        else:
            print("player lost")
    else:
        if(doors[choice]=='Goat'):
            print("Player lost")
        else:
            print("player wins")
            #dont_swap=dont_swap+1
            win=win+1
    j=j+1
print(win)
#print(swap)
#print(dont_swap)