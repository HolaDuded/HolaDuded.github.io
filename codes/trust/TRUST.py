from random import randint as r
def roll():
    doubles=False
    roll1=r(1,6)
    roll2=r(1,6)
    if roll1==roll2:
        doubles=True
    return roll1,roll2,doubles
print("Welcome to TRUST")
playagain=""
advanc="n"
while playagain.lower()!="n":
    if advanc.lower()=="y":
        ad=True
    elif advanc.lower()=="n":
        ad=False
    ynnames=input("Would you like custom names (y/n) : ")
    if ynnames.lower()=="y":
        play1=input("Enter Player One's custom name: ")
        play2=input("Enter Player Two's custom name: ")
    else:
        play1="Player One"
        play2="Player Two"
    advanc="n"
    play1mon=1500
    play2mon=1500
    turn=1
    playagain=""
    spaces=["Go","Mediterranean Avenue","Neighborhood Chest","Baltic Avenue","Income Tax","Reading Railroad","Oriental Avenue","Chance","Vermont Avenue","Connecticut Avenue","Visiting Jail","St. Charles Place","Electric Company","States Avenue","Virginia Avenue","Pennsylvania Railroad","St. James Place","Neighborhood Chest","Tennessee Avenue","New York Avenue","Parking Lot","Kentucky Avenue","Fortune","Indiana Avenue","Illinois Avenue","B+O Railroad","Atlantic Avenue","Vermont Avenue","Water Works","Marvin Gardens","Parking Lot","Pacific Avenue","North Carolina Avenue","Neighborhood Chest","Pennsylvania Avenue","Short Line","Fortune","Park Place","Luxury Tax","Boardwalk"]
    avaprop=["Mediterranean Avenue","Baltic Avenue","Reading Railroad","Oriental Avenue","Vermont Avenue","Connecticut Avenue","St. Charles Place","Electric Company","States Avenue","Virginia Avenue","Pennsylvania Railroad","St. James Place","Tennessee Avenue","New York Avenue","Kentucky Avenue","Indiana Avenue","Illinois Avenue","B+O Railroad","Atlantic Avenue","Vermont Avenue","Water Works","Marvin Gardens","Pacific Avenue","North Carolina Avenue","Pennsylvania Avenue","Short Line","Park Place","Boardwalk"]
    allprop=["Mediterranean Avenue","Baltic Avenue","Reading Railroad","Oriental Avenue","Vermont Avenue","Connecticut Avenue","St. Charles Place","Electric Company","States Avenue","Virginia Avenue","Pennsylvania Railroad","St. James Place","Tennessee Avenue","New York Avenue","Kentucky Avenue","Indiana Avenue","Illinois Avenue","B+O Railroad","Atlantic Avenue","Vermont Avenue","Water Works","Marvin Gardens","Pacific Avenue","North Carolina Avenue","Pennsylvania Avenue","Short Line","Park Place","Boardwalk"]
    propcosts=[60,60,200,100,100,120,140,150,140,160,200,180,180,200,220,220,240,200,260,260,150,280,300,300,320,200,350,400]
    proprent=[2,4,100,6,6,8,10,10,10,12,100,14,14,16,18,18,20,100,22,22,10,24,26,26,28,100,35,50]
    play1prop=[]
    play2prop=[]
    bankrupt1=False
    bankrupt2=False
    where1is=0
    where2is=0
    play1jail=False
    play2jail=False
    jails1=0
    jails2=0
    while not(bankrupt1) and not(bankrupt2):
        if play1mon<=0:
            bankrupt1=True
        if play2mon<=0:
            bankrupt2=True
        if turn==1 and not(bankrupt1) and not(bankrupt2):
            print("\n"+play1+"\n")
            print("Money: "+str(play1mon))
            print("Properties: ",end="")
            for x in range(len(play1prop)):
                print(str(play1prop[x]),end=", ")
            print()
            do=""
            rollcomplete=False
            rols=0
            doubles=0
            while do.lower()!="pass" or not(rollcomplete):
                do=input("What would you like to do? (roll, buy, trade, pass (You must roll before passing)) ")
                if do.lower()=="roll":
                    if not(rollcomplete):
                        rols+=1
                        rollcomplete=True
                        rolls=roll()
                        if rolls[2]:
                            rollcomplete=False
                            doubles+=1
                        print("You got a "+str(rolls[0])+" and a "+str(rolls[1])+"\nYou have moved "+str(rolls[0]+rolls[1])+" spaces.")
                        if not(play1jail):
                            where1is+=rolls[0]+rolls[1]
                        if where1is>=40:
                            where1is-=40
                            play1mon+=200
                        print("You are now on "+spaces[where1is])
                        if spaces[where1is]=="Fortune":
                            print("\nFortune\nYou recieve $150.  Congratulations.\n")
                            play1mon+=150
                        if spaces[where1is]=="Neighborhood Chest":
                            print("\nCommunity Chest\nYou recieve $250.  Congratulations.\n")
                            play1mon+=250
                        if spaces[where1is] in play2prop and rols>0:
                            spot=allprop.index(spaces[where1is])
                            rent=proprent[spot]
                            play1mon-=rent
                            play2mon+=rent
                            print("You landed on "+spaces[where1is]+".  You owe "+play2+" $"+str(rent)+".")
                        if spaces[where1is]=="Go":
                            play1mon+=200
                        if spaces[where1is]=="Luxury Tax":
                            play1mon-=75
                            print("You landed on Luxury Tax.  You owe $75.  You now have $"+str(play1mon)+" remaining.")
                        if spaces[where1is]=="Income Tax":
                            whatdo=int(input("Would you like to pay 10% or $200 (10/200): "))
                            if whatdo==10:
                                monowe=int(play1mon*0.1)
                            if whatdo==200:
                                monowe=200
                            print("You landed on Income Tax.  You owe $"+str(monowe)+".  You have $",end="")
                            play1mon-=monowe
                            print(str(play1mon)+" remaining.")
                        #if spaces[where1is]=="Go To Jail":
                            #play1jail=True
                elif do.lower()=="buy":
                    if rols>0 and spaces[where1is] in avaprop:
                        space=allprop.index(spaces[where1is])
                        play1prop.append(spaces[where1is])
                        avaprop.remove(spaces[where1is])
                        play1mon-=propcosts[space]
                        print("\nYou have bought "+str(spaces[where1is])+" for $"+str(propcosts[space])+".  You have $"+str(play1mon)+" remaining.\n")
                elif do.lower()=="trade":
                    otherplayagree=input(play2+", do you want to trade? (y/n) ")
                    if otherplayagree.lower()=="y":
                        trade=input(play1+", what property would you like to trade? ")
                        if trade in play1prop:
                            agree=input(play2+", do you agree to this trade? (y/n) ")
                            if agree.lower()=="y":
                                otheroffer=input(play2+", what property do you offer? ")
                                if otheroffer in play2prop:
                                    agree=input(play1+", do you agree to this offer? (y/n) ")
                                    if agree.lower()=="y":
                                        play1prop.remove(trade)
                                        play2prop.append(trade)
                                        play2prop.remove(otheroffer)
                                        play1prop.append(otheroffer)
                                    else:
                                        print("Sorry, trade denied.")
                                else:
                                    print("Sorry, trade denied.")
                            else:
                                print("Sorry, trade denied.")
                        else:
                            print("Sorry, trade denied.")
                    else:
                        print("Sorry, trade denied.")
            turn=2
        if play1mon<=0:
            bankrupt1=True
        if play2mon<=0:
            bankrupt2=True
        elif turn==2 and not(bankrupt1) and not(bankrupt2):
            print("\n"+play2+"\n")
            print("Money: "+str(play2mon))
            print("Properties: ",end="")
            for x in range(len(play2prop)):
                print(str(play2prop[x]),end=", ")
            print()
            do=""
            rollcomplete=False
            rols=0
            doubles=0
            while do.lower()!="pass" or not(rollcomplete):
                do=input("What would you like to do? (roll, buy, trade, pass (You must roll before passing))) ")
                if do.lower()=="roll" and not(rollcomplete):
                    rols+=1
                    rollcomplete=True
                    rolls=roll()
                    if rolls[2]:
                        rollcomplete=False
                        doubles+=1
                    print("You got a "+str(rolls[0])+" and a "+str(rolls[1])+"\nYou have moved "+str(rolls[0]+rolls[1])+" spaces.")
                    if not(play2jail):
                        where2is+=rolls[0]+rolls[1]
                    if where2is>=40:
                        where2is-=40
                        play2mon+=200
                    print("You are now on "+spaces[where2is])
                    if spaces[where2is]=="Fortune":
                        print("\nFortune\nYou recieve $150.  Congratulations.\n")
                        play2mon+=150
                    if spaces[where2is]=="Neighborhood Chest":
                        print("\nNeighborhood Chest\nYou recieve $250.  Congratulations.\n")
                        play2mon+=250
                    if spaces[where2is] in play1prop and rols>0:
                        spot=allprop.index(spaces[where2is])
                        rent=proprent[spot]
                        play2mon-=rent
                        play1mon+=rent
                        print("You landed on "+spaces[where2is]+".  You owe "+play1+" $"+str(rent)+".")
                    if spaces[where2is]=="Go":
                        play2mon+=200
                    if spaces[where2is]=="Luxury Tax":
                        play2mon-=75
                        print("You landed on Luxury Tax.  You owe $75.  You now have $"+str(play2mon)+" remaining.")
                    if spaces[where2is]=="Income Tax":
                        whatdo=int(input("Would you like to pay 10% or $200 (10/200): "))
                        if whatdo==10:
                            monowe=int(play2mon*0.1)
                        if whatdo==200:
                            monowe=200
                        print("You landed on Income Tax.  You owe $"+str(monowe)+".  You have $",end="")
                        play2mon-=monowe
                        print(str(play2mon)+" remaining.")
                elif do.lower()=="buy":
                    if rols>0 and spaces[where2is] in avaprop:
                        space=allprop.index(spaces[where2is])
                        play2prop.append(spaces[where2is])
                        avaprop.remove(spaces[where2is])
                        play2mon-=propcosts[space]
                        print("\nYou have bought "+str(spaces[where2is])+" for $"+str(propcosts[space])+".  You have $"+str(play2mon)+" remaining.\n")
                elif do.lower()=="trade":
                    otherplayagree=input(play1+", do you want to trade? (y/n) ")
                    if otherplayagree.lower()=="y":
                        trade=input(play2+", what property would you like to trade? ")
                        if trade in play2prop:
                            agree=input(play1+", do you agree to this trade? (y/n) ")
                            if agree.lower()=="y":
                                otheroffer=input(play1+", what property do you offer? ")
                                if otheroffer in play1prop:
                                    agree=input(play2+", do you agree to this offer? (y/n) ")
                                    if agree.lower()=="y":
                                        play2prop.remove(trade)
                                        play1prop.append(trade)
                                        play1prop.remove(otheroffer)
                                        play2prop.append(otheroffer)
                                    else:
                                        print("Sorry, trade denied.")
                                else:
                                    print("Sorry, trade denied.")
                            else:
                                print("Sorry, trade denied.")
                        else:
                            print("Sorry, trade denied.")
                    else:
                        print("Sorry, trade denied.")
            turn=1
    if bankrupt1:
        print("\n\n"+play2+" wins!\n")
    if bankrupt2:
        print("\n\n"+play1+" wins!\n")
    playagain=input("Would you like to play again (y/n): ")
