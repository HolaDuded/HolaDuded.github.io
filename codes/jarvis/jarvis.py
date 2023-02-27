import pyttsx3
import speech_recognition as sr
import datetime
from pyfiglet import figlet_format
from os import system,startfile,getenv
import smtplib
import wikipedia
from time import *
import webbrowser
from sys import stdout
from dotenv import load_dotenv
load_dotenv()
class Loader:
    def __init__(self, desc="Loading...",end="Done!",timeout=0.1):
        from threading import Thread
        self.desc=desc
        self.end=end
        self.timeout=timeout
        self._thread=Thread(target=self._animate, daemon=True)
        self.steps=["⢿ ","⣻ ","⣽ ","⣾ ","⣷ ","⣯ ","⣟ ","⡿ "]
        self.done=False
    def start(self):
        self._thread.start()
        return self
    def _animate(self):
        from itertools import cycle
        from sty import fg,bg,ef,rs
        import time
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}"+fg.rs,flush=True,end="")
            time.sleep(self.timeout)
    def __enter__(self):
        self.start()
    def stop(self):
        from shutil import get_terminal_size
        from sty import fg,bg,ef,rs
        self.done=True
        cols=get_terminal_size((80,20)).columns
        print("\r"+" "*cols,end="",flush=True)
        print(f"\r{self.end}"+fg.rs,flush=True)
    def __exit__(self,exc_type,exc_value,tb):
        self.stop()
jarglis=figlet_format("Jarvis   2 . 0")
EMAIL=getenv("EMAIL")
PASSWORD=getenv("PASS")
def take_commands(coax="Listening "):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        l=Loader(coax,"",0.05).start()
        Speak(coax)
        #r.pause_threshold=0.7
        audio=r.listen(source)
        l.stop()
        stdout.write("\x1b[1A")
        try:
            l=Loader("Scanning for words ","",0.05).start()
            Speak("Scanning for words")
            Query=r.recognize_google(audio)
            l.stop()
            stdout.write("\x1b[1A")
            pas("You said: "+str(Query))
        except Exception as e:
            print(e)
            pas("Please say that again?")
            return "None"
    l.stop()
    return Query
def sendEmail(to,subject,content):
    sting="                    "*25
    msg="Subject: {}\n\n{}".format(subject,content)
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL,PASSWORD)
    try:
        server.sendmail(EMAIL,to,msg+sting+"This message sent by custom voice assistent.")
    except Exception as e:
        pas(e)
    server.close()
def Speak(audio):
    engine=pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
def pas(text):
    print(text)
    Speak(text)
def logo():
    print(jarglis)
def clear():
    system("cls")
    logo()
def load(start="",end="",timer=0.05,times=5):
    l=Loader(start,end,timer).start()
    sleep(times)
    l.stop()
if __name__=="__main__":
    locatname="C:\\Users\\User\\OneDrive\\Desktop\\Programming\\Python Files\\Python Projects\\virtual_assistant\\jarvis_logs\\"
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        greeting="Good morning"
    elif hour>=12 and hour<18:
        greeting="Good afternoon"
    else:
        greeting="Good evening"
    jarname="Jarvis"
    USER=""
    clear()
    load("Initializing ","",0.05,2.5)
    clear()
    pas(greeting+" "+USER+".  It is me, "+jarname+", your personal assistant.  How may I assist you today?")
    peopleemailnames=[getenv("name1"),getenv("name2"),getenv("name3"),getenv("name4"),getenv("name5"),getenv("name6"),getenv("name7"),getenv("name8"),getenv("name9"),]
    peopleemails=[getenv("email1"),getenv("email2"),getenv("email3"),getenv("email4"),getenv("email5"),getenv("email6"),getenv("email7"),getenv("email8"),getenv("email9")]
    commands=["hello","goodbye","how are you","am I useful"]
    commandsoutput=["Hello","No","Good.  What about you?","Yes, of course.  You made me, after all."]
    clear()
    while True:
        command=take_commands()
        command=command.lower()
        name=datetime.datetime.now().strftime("%D")
        name=name.replace("/","-",name.count("/"))
        with open(locatname+name+"_log.txt","a") as file:
            file.write(datetime.datetime.now().strftime("%H:%M:%S")+" - "+command+"\n")
        if "" in command:
            if "exit" in command:
                pas("Shuting Down")
                clear()
                exit()
            elif commands[0] in command:
                pas(commandsoutput[0])
            elif commands[1] in command:
                pas(commandsoutput[1])
            elif commands[2] in command:
                pas(commandsoutput[2])
            elif commands[3] in command:
                pas(commandsoutput[3])
            elif "send an email to" in command:
                command=command.replace("jarvis","",command.count("jarvis "))
                command=command.replace("send","",command.count("send "))
                command=command.replace("an","",command.count("an "))
                command=command.replace("email","",command.count("email "))
                command=command.replace("to","",command.count("to "))
                if command.strip() not in peopleemailnames:
                    pas("Unrecognized person")
                elif command in peopleemailnames:
                    to=peopleemails[peopleemailnames.index(command.strip())]
                    subject=take_commands("what should the subject be?")
                    message=take_commands("what should the message be?")
                    try:
                        sendEmail(to,subject,message)
                    except Exception as e:
                        Speak("Error")
                        input(e)
                    pas("Mail sent")
            elif "wikipedia" in command:
                l=Loader("Searching Wikipedia "," ",0.05).start()
                Speak("Searching Wikipedia")
                command=command.replace("wikipedia","")
                if "search" in command:
                    command=command.replace("search ","")
                if "for" in command:
                    command=command.replace("for ","")
                try:
                    results=wikipedia.summary(command)
                except Exception as e:
                    Speak("Error")
                    results=""
                    input(e)
                l.stop()
                Speak("Search Results Printed")
                input(results)
            elif "open youtube" in command:
                webbrowser.get("c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("youtube.com")
            elif "open google" in command:
                webbrowser.get("c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("google.com")
            elif "open spotify" in command:
                webbrowser.open_new("C:\\Users\\User\\AppData\\Local\Microsoft\\WindowsApps\\Spotify.exe")
            elif "open netflix" in command:
                webbrowser.open_new("C:\\Users\\User\\AppData\\Local\Microsoft\\WindowsApps\\Netflix.exe")
            elif "what is the time" in command or "what's the time" in command:
                pas(datetime.datetime.now().strftime("%H:%M:%S"))
            elif "what is the date" in command or "what's the date" in command:
                pas(datetime.datetime.now().strftime("%D"))
            else:
                pas("Unknown command")
        else:
            pas("Unknown intelligence")
        clear()