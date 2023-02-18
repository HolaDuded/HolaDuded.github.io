from secrets import choice
from random import randint
from time import *
from types import NoneType
from lazyt import Loader
def time_convert(sec):
    mins=sec//60
    sec=sec%60
    hours=mins//60
    mins=mins%60
    return hours,mins,sec
def writefile(numplayers,timelapsed):
    with open('lifeanalytics.txt','r') as txt:
        txt=txt.readlines()
        txt[0]=txt[0][:-1]
        times=txt[0].split("|")
        players=txt[1].split("|")
    times.append(str(timelapsed))
    players.append(str(numplayers))
    times.sort()
    players.sort()
    with open('lifeanalytics.txt','w') as txt:
        txt.write('|'.join(times)+"\n")
        txt.write('|'.join(players))
def moneychange(moneys,pin,tipe,val):
    money=moneys[pin]
    moneys.remove(money)
    if tipe=="+":
        money+=val
    elif tipe=="-":
        money-=val
    moneys.insert(pin,money)
def pase():
    actgh=None
    acfg=actgh[4]
def tprint(srt,time=0.025):
    for char in srt:
        print(char,end="")
        sleep(time)
    print()
def tinput(srt,time=0.025,space=""):
    for char in srt:
        print(char,end="")
        sleep(time)
    entered=input(space)
    return entered
def spiner(min=1,max=10):
    return randint(min,max)
def get_action_doer(action,all_actions):
    if action=="":
        action=choice(all_actions)
    action=action.split("\n")
    if "PAY BANK" in action[-1]:
        action=action[-1]
        action=action.replace("PAY BANK ","")
        action=action.replace(",","")
        return "-"+str(action)
    if "COLLECT" in action[-1] and "FROM BANK" in action[-1]:
        action=action[-1]
        action=action.replace("COLLECT ","")
        action=action.replace(" FROM BANK","")
        action=action.replace(",","")
        return "+"+str(action)
all_actions=[
    "It's Great Uncle Max's 100th birthday!\nThrow the party of a lifetime!\nPAY BANK 30,000",
    "Sell flowers from your garden!\nName your favorite flower.\nCOLLECT 70,000 FROM BANK",
    "Buy a priceless painting!\nTell everyone what it looks like.\nPAY BANK 50,000",
    "Buy a home cinema!\nName your favorite movie.\nPAY BANK 50,000",
    "Buy a designer suit!\nLooking good!\nPAY BANK 30,000",
    "Write a children's book!\nTell everyone what it's about.\nCOLLECT 40,000 FROM BANK",
    "Start a family band!\nWhat would everybody play?\nPLAY BANK 30,000",
    "Climb Mount Everest!\nPAY BANK 30,000",
    "Win a skateboarding competition!\nShow everyone your moves.\nCOLLECT 100,000 FROM BANK",
    "Sail around the world!\nTell everyone where you're going.\nPAY BANK 50,000",
    "Make your yard an adventure playground!\nPAY BANK 30,000",
    "Pass your driving test!\nTell everyone what car you got.\nPAY BANK 50,000",
    "Get a pool!\nIt's time for scorching summer fun.\nPAY BANK 50,000",
    "Your pet goat wins a ribbon!\nTell everyone its name.\nCOLLECT 120,000 FROM BANK",
    "Win \"Family of the Year\" award!\nHug everyone to say thanks.\nCOLLECT 40,000 FROM BANK",
    "Learn to skydive!\nThat's one long free fall\nPAY BANK 70,000",
    "Give money to animal rescue!\nName your favorite animal.\nPAY BANK 20,000",
    "Win a \"Beautiful Forehead\" Contest!\nTell everyone why your forehead's the prettiest.\nCOLLECT 40,000 FROM BANK",
    "Build a maze!\nEveryone loves it!\nCOLLECT 50,000 FROM BANK",
    "Tax refund!\nHooray!\nCOLLECT 50,000 FROM BANK",
    "Start a snail farm!\nShells are the future.\nPAY BANK 50,000",
    "Set up a school!\nEveryone wants to go there!\nCOLLECT 40,000 FROM BANK",
    "Buy a tropical aquarium!\nName your fish.\nPAY BANK 20,000",
    "Trace your family tree!\nDiscover a family fortune.\nCOLLECT 70,000 FROM BANK"
]
again=""
fancy=tinput("Enable fancy output (y/n)? ").lower()
if fancy!="y":
    def tprint(srt):
        print(srt)
    def tinput(srt):
        return input(srt)
while again!="q":
    playnum=int(tinput("How many players are playing: "))
    while playnum<=1:
        tprint("Invalid option\nPlease choose a number greater than one")
        playnum=int(tinput("How many players are playing: "))
    starttime=time()
    all_at_end=False
    retired=[]
    spaces=[]
    players=[]
    moneys=[]
    jobs=[]
    actions=[]
    avajobs=[100000,80000,130000,100000,100000,120000,110000,100000]
    avajobname=["Scientist","Fashion Designer","Doctor","Teacher","Secret Agent","Lawyer","Video Game Designer","Veterinarian"]
    paydays=[15,20,30,41,47,54,62,74,84,93,99,104]
    spintowin=[18,32,50,68,78,95]
    houses=[34,45,53,59,73,82,98]
    graduated=[]
    donepaydays=[]
    line="\n+---------------------------+\n"
    graduate=11 #getting fully added later
    #married=24 #getting added later
    for name in range(playnum):
        players.append(tinput("Enter player name: "))
        spaces.append(0)
        moneys.append(0)
        jobs.append(0)
        actions.append([])
        donepaydays.append([])
    while all_at_end==False:
        for player in players:
            if player not in retired:
                pin=players.index(player)
                tprint(line+"  "+players[pin]+"\'s turn")
                #whatdo=tinput("What do you want to do? ")
                spin=spiner()
                tprint("  You spun a "+str(spin))
                ospace=spaces[pin]
                #print(ospace)
                spaces[pin]+=spin
                space=spaces[pin]
                #print(space)
                rspace=[]
                tprint("  You are now on space #"+str(space))
                for x in range(space+1,ospace+1):
                    print(x)
                    rspace.append(x)
                #print(rspace)
                if space>=graduate:
                    if pin not in graduated:
                        space=graduate
                        chosenjob=choice(avajobs)
                        tprint("  You are now a "+str(avajobname[avajobs.index(chosenjob)])+"!\n  You make $"+str(chosenjob)+" per payday.")
                        jobs.remove(jobs[pin])
                        jobs.insert(pin,chosenjob)
                        graduated.append(pin)
                for payday in paydays:
                    if space>=payday:
                        if payday not in donepaydays[pin]:
                            donepaydays[pin].append(payday)
                            moneychange(moneys,pin,"+",int(jobs[pin]))
                            tprint("\n\tPAYDAY\n\nYou have earned $"+str(jobs[pin])+", which gives you a total of $"+str(moneys[pin]))
                if space in spintowin:
                    tprint("\n\tSPIN TO WIN\n")
                    if playnum>10:
                        maxspin=playnum
                    else:
                        maxspin=10
                    spins=[]
                    for payer in players:
                        spinned=spiner(1,maxspin)
                        while spinned in spins:
                            spinned=spiner(1,maxspin)
                        spins.append(spinned)
                    masterspin=spiner(1,maxspin)
                    while masterspin not in spins:
                        masterspin=spiner(1,maxspin)
                    for x in range(len(spins)):
                        if spins[x]==masterspin:
                            spinpin=x
                    moneychange(moneys,spinpin,"+",200000)
                    tprint("  "+players[spinpin]+" has won $200000, which gives them a new total of $"+str(moneys[spinpin])+"\n")
                if space in houses:
                    pass
                if space not in spintowin and space not in houses and space not in paydays:
                    action=None
                    while type(action)==NoneType:
                        action=choice(all_actions)
                        actions[pin].append(action)
                        action=get_action_doer(action,all_actions)
                    tprint("\n\tAction\n\n"+str(actions[pin][-1])+"\n")
                    if action[0]=="+":
                        moneychange(moneys,pin,"+",int(action[1:]))
                    if action[0]=="-":
                        moneychange(moneys,pin,"-",int(action[1:]))
                tprint("  You have $"+str(moneys[pin]))
                #tinput()
            for plyer in range(playnum):
                if int(spaces[plyer])>=108:
                    if players[plyer] not in retired:
                        retired.append(players[plyer])
                        actionnum=len(actions[plyer])
                        moneychange(moneys,plyer,"+",actionnum*100000)
            if len(retired)==playnum:
                all_at_end=True
    tprint(line)
    for player in players:
        tprint(player+" had $"+str(moneys[players.index(player)]))
    winamo=max(moneys)
    playwin=moneys.index(winamo)
    tprint(str(players[playwin])+" has won the game with $"+str(winamo)+"!")
    endtime=time()
    timelapsed=endtime-starttime
    hours,mins,sec=time_convert(timelapsed)
    tprint(str(hours)+":"+str(mins)+":"+str(sec))
    writefile(playnum,round(timelapsed,2))
    tprint("\n+----------------------------------------+")
    again=tinput("| Press ENTER to continue, q to quit: ")
    tprint("+----------------------------------------+\n")
analytics=tinput("Would you like to view analytics data (y/n)? ").lower()
if analytics=="y":
    def tprint(srt,time=0.025):
        for char in srt:
            print(char,end="")
            sleep(time)
    print()
    def tinput(srt,time=0.025,space=""):
        for char in srt:
            print(char,end="")
            sleep(time)
        entered=input(space)
        return entered
    l=Loader("Importing Analytics ","",0.05)
    print()
    import Game_Of_Life_Analytics_Code
    print()
tprint("Thanks for playing!")