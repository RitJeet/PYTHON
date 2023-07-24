import webbrowser
import pyttsx3
import speech_recognition as s_r
import datetime
import wikipedia
from pytube import YouTube
import requests
from bs4 import BeautifulSoup
import time as t
import os
eng=pyttsx3.init('sapi5')
voices=eng.getProperty('voices')
eng.setProperty('voice',voices[0].id)
def speak(audio):
    eng.say(audio)
    eng.runAndWait()
def wishes():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 4 :
        speak("This is midnight sir plzz go to bed.")
    elif hour >= 4 and hour < 10 :
        speak("Good Morning sir")
    elif hour >= 10 and hour < 15 :
        speak("Good Noon sir")
    elif hour >= 15 and hour <= 21 :
        speak("Good evening sir")
    else :
        speak ("Good night sir")
def command():
    r=s_r.Recognizer()
    with s_r.Microphone() as source :
        #os.system("cls")
        print("Listening.....")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User say: {query}")
    except:
        print("Say once again")
        return "None"
    return query
if __name__=="__main__":
    speak("Hi,Jeet,How can I help you??")
    c=1
    wishes()
    while c==1:
        query=command().lower()
        if 'wikipedia' in query:
            speak("Searching in wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'what is your name' in query:
            speak("My name is Python sir")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'what is your father name' in query:
            speak("My father name is Jeet Ganguly sir!")
            print("My father name is Jeet Ganguly sir")
        elif 'what is your mother name' in query:
            speak("My mother name is Rittwika Ganguly sir!")
            print("My mother name is Rittwika Ganguly sir!")
        elif 'search in youtube' in query:
            query=query.replace("search in youtube","")
            #channel=command().lower()            
            res="https://www.youtube.com/results?search_query="+query
            webbrowser.open(res)
        elif 'search in google' in query:
            query=query.replace("search in google","")
            resu=f"https://www.google.com/search?q={query}&source=hp&ei=GA6-ZLDuE6fS1e8P_uWoqA8&iflsig=AD69kcEAAAAAZL4cKDQ9Xf0Znc934VowkrOP4P5Jb0jP&ved=0ahUKEwiw2sqU0KaAAxUnafUHHf4yCvUQ4dUDCAk&uact=5&oq=buffon&gs_lp=Egdnd3Mtd2l6IgZidWZmb24yCxAuGIMBGLEDGIAEMggQABiABBixAzILEAAYgAQYsQMYgwEyBRAAGIAEMgUQABiABDIFEAAYgAQyBxAAGIAEGAoyBRAAGIAEMgUQABiABDIFEAAYgARImw1QAFizCXAAeACQAQCYAYkCoAHWCaoBBTAuMy4zuAEDyAEA-AEBwgILEC4YgwEYsQMYigXCAgsQLhiKBRixAxiDAcICCxAuGIAEGLEDGIMBwgIREC4YigUYsQMYgwEYxwEY0QPCAggQLhiABBixA8ICDhAAGIAEGLEDGIMBGMkDwgIIEC4YsQMYgAQ&sclient=gws-wiz"
            webbrowser.open(resu)
        elif 'download youtube video' in query:
            speak("I can download high quality video from you tube")
            #speak("Please give me the link of vieo")
            link=input("Enter the link: ")
            YouTube(link).streams.get_highest_resolution().download("D:/")
        elif 'goodbye' in query:
            speak("Good bye sir, I am always with you")
            print("Good bye sir, I am always with you")
            c=c+1
            
        elif 'stop' in query:
            speak("Ok sir I am stop ")
            c=c+1
        elif 'weather' in query or 'temperature' in query:
            search='temperature in kolaghat'
            url=f"https://www.google.com/search?q={search}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")
            print(f"current {search} is {temp}")
        elif 'how are you' in query:
            speak("I am fine sir, And you?")
            print("I am fine sir, And you?")
        elif 'fine' in query or 'good' in query:
            speak(f"I am very happy because you are {query}")
            print(f"I am very happy because you are {query}")
        elif 'current time' in query:
            timestamp=t.strftime("%H:%M")
            speak(f"Now current time is {timestamp}")
            print(f"Now current time is {timestamp}")
           

            
        
    

